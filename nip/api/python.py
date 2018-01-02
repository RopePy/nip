import os
from functools import wraps
from subprocess import call
from venv_tools import Venv

from nip.config import paths


def create_venv():
    return call(f'python3 -m venv {paths.PYTHON_MODULES_PATH}', shell=True)


def call_command(command):
    return call(command, shell=True)


def call_command_from_cwd(command):
    return call(command, cwd=os.getcwd(), shell=True)


def call_command_from_venv(command, env_dir=paths.PYTHON_MODULES_PATH):
    with Venv(env_dir):
        return call_command_from_cwd(command)


def venv_context_wrapper(func, env_dir):
    @wraps(func)
    def inner(*args, **kw):
        with Venv(env_dir):
            func(*args, **kw)
    return inner
