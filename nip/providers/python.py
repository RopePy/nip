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


def with_venv(function, env_dir=paths.PYTHON_MODULES_PATH):
    @wraps(function)
    def inner(*args, **kw):
        with Venv(env_dir):
            function(*args, **kw)
    return inner


@with_venv
def call_command_from_venv(command):
    return call_command_from_cwd(command)
