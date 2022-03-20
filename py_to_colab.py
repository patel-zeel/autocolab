import re
from importlib_metadata import metadata
import jupytext
from glob import glob
from nbformat.notebooknode import NotebookNode

scripts = glob("scripts/*.py")

def src_func(path):
    return f"<a href=\"https://colab.research.google.com/github/patel-zeel/autocolab/blob/main/{path}\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"

for script in scripts:
    content = jupytext.read(script)
    
    new_file = script.replace("scripts", "notebooks")
    new_file = re.sub(r"\.py$", ".ipynb", new_file)
       
    src = [src_func(new_file)]
    colab_cell = NotebookNode(
                cell_type="markdown",
                metadata=NotebookNode(),
                source=src
                )
    content['cells'].insert(0, colab_cell)
    # Write content to a jupyter notebook
    # Replace file extension with .ipynb using regular expression
    jupytext.write(content, new_file, fmt="ipynb")
    