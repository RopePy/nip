import os
from os.path import join

from nip.config import defaults


def get_basename():
    return os.path.basename(os.getcwd().rstrip('/'))


def directory_is_empty(target_dir):
    if os.path.exists(target_dir):
        for _, folders, files in os.walk(target_dir):
            return False if (files or folders) else True
    else:
        return True


def current_working_directory_is_empty():
    return directory_is_empty(os.getcwd())


def get_nipfile_path(env=defaults):
    return join(os.getcwd(), env.NIPFILE)


def get_python_setup_py_path(env=defaults):
    return join(os.getcwd(), env.PYTHON_SETUP_PY)


def get_gitignore_path(env=defaults):
    return join(os.getcwd(), env.GITIGNORE)


def get_requirements_path(env=defaults):
    return join(os.getcwd(), env.REQUIREMENTS_FILE)


def get_dev_requirements_path(env=defaults):
    return join(os.getcwd(), env.DEV_REQUIREMENTS_FILE)


def get_python_modules_path(env=defaults):
    return join(os.getcwd(), env.PYTHON_MODULES)


def get_python_modules_bin_path(env=defaults):
    return join(get_python_modules_path(env), 'bin')


def get_pip_executable_path(env=defaults):
    return join(get_python_modules_bin_path(env), env.PIP)


def get_python_executable_path(env=defaults):
    return join(get_python_modules_bin_path(env), env.PYTHON)


def file_write_lines(lines, to):
    with open(to, 'w+') as fs:
        fs.write("\n".join(lines))
