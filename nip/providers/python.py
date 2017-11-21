import os
from nip.config import paths

__all__ = ['create_venv', 'call_python_command_from_venv']


def create_venv():
    os.system(f'python3 -m venv {paths.PYTHON_MODULES_PATH}')

def call_python_command_from_venv(command):
    os.system(f'{paths.PYTHON_MODULES_BIN_PATH}/{command}')
