from venv_tools import Venv

from nip.config import defaults
from nip.providers.shell import call_command_from_cwd
from nip.utils.path import get_python_modules_path


def create_venv(env):
    call_command_from_cwd(f'python3 -m venv {env.PYTHON_MODULES}')


def call_command_from_venv(command, env=defaults):
    py_modules_path = get_python_modules_path(env)
    with Venv(py_modules_path):
        return call_command_from_cwd(command)
