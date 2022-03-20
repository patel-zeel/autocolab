import os
import re
import jupytext
from glob import glob
from nbformat.notebooknode import NotebookNode

base_path = os.getcwd()
scripts = glob(base_path + "/scripts/*.py")
print("full path", base_path + "/scripts/*.py")
print("scripts:", scripts)


def src_func(path):
    return f'<a href="https://colab.research.google.com/github/patel-zeel/autocolab/blob/main/{path}" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>'


if not os.path.exists("notebooks"):
    os.mkdir(base_path + "/notebooks")

for script in scripts:
    content = jupytext.read(script)

    new_file = script.replace("/scripts/", "/notebooks/")
    new_file = re.sub(r"\.py$", ".ipynb", new_file)

    src = [src_func(new_file)]
    colab_cell = NotebookNode(cell_type="markdown", metadata=NotebookNode(), source=src)
    content["cells"].insert(0, colab_cell)
    # Write content to a jupyter notebook
    # Replace file extension with .ipynb using regular expression
    jupytext.write(content, new_file, fmt="ipynb")
    assert os.path.exists(new_file)
