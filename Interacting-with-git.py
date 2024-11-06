# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: conda_python3
#     language: python
#     name: conda_python3
# ---

# %cd /home/ec2-user/SageMaker/


# !git clone https://github.com/qualiaMachine/AWS_helpers.git # downloads AWS_helpers folder/repo (refresh file explorer to see)


# +
import getpass

# Prompt for GitHub username and PAT securely
username = input("GitHub Username: ")
token = getpass.getpass("GitHub Personal Access Token (PAT): ")
# -

# !git config --global user.name "qualiaMachine"
# !git config --global user.email endeman@wisc.edu

# !pip install jupytext


# !jupytext --to py Interacting-with-S3.ipynb


# +
import subprocess
import os

# List all .ipynb files in the directory
notebooks = [f for f in os.listdir() if f.endswith('.ipynb')]

# Convert each notebook to .py using jupytext
for notebook in notebooks:
    output_file = notebook.replace('.ipynb', '.py')
    subprocess.run(["jupytext", "--to", "py", notebook, "--output", output_file])
    print(f"Converted {notebook} to {output_file}")
# -



# +

import AWS_helpers.helpers as helpers

# Reload the module
import importlib
importlib.reload(helpers)

helpers.convert_files(direction="notebook_to_python")
# -

# %cd AWS_helpers


