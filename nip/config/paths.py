from os.path import join
from nip.utils.path import __dirname


# Python Modules
PYTHON_MODULES = 'python_modules'
PYTHON_MODULES_PATH = join(__dirname, PYTHON_MODULES)
PYTHON_MODULES_BIN_PATH = join(__dirname, PYTHON_MODULES_PATH, 'bin')

PYTHON_SETUP_PY = 'setup.py'
PYTHON_SETUP_PY_PATH = join(__dirname, PYTHON_SETUP_PY)


# Python
PYTHON = 'python'
PYTHON_MODULES_PYTHON_EXEC = join(PYTHON_MODULES_BIN_PATH, PYTHON)


# Pip
PIP = 'pip'
PYTHON_MODULES_PIP_EXEC = join(PYTHON_MODULES_BIN_PATH, PIP)

# Requirements
REQUIREMENTS_FILE = 'requirements.txt'
DEV_REQUIREMENTS_FILE = 'dev_requirements.txt'
REQUIREMENTS_PATH = join(__dirname, REQUIREMENTS_FILE)
DEV_REQUIREMENTS_PATH = join(__dirname, DEV_REQUIREMENTS_FILE)


# Nip
NIPFILE = 'nip.json'
NIPFILE_PATH = join(__dirname, NIPFILE)


# Git
GIT = 'git'
GITIGNORE = '.gitignore'
GITIGNORE_PATH = join(__dirname, GITIGNORE)
