import os
from nip.config import paths
from nip.utils.spinner import create_spinner


__all__ = ['pip_install', 'pip_install_version', 'pip_uninstall']

PIP_EXEC = paths.PYTHON_MODULES_PIP_EXEC

def pip_install(package):
    return pip_install_version(package, version=None)

def pip_freeze():
    """ pip freeze > requirements.txt """
    os.system(f'{PIP_EXEC} freeze > {paths.REQUIREMENTS_PATH}')

def silent_pip_freeze():
    """ pip freeze > requirements.txt """
    os.system(f'{PIP_EXEC} freeze > {paths.REQUIREMENTS_PATH} -qqq')


def pip_install_version(package, version=None):
    os.system(f'{PIP_EXEC} install {package}{version or ""}')


def silent_pip_install_version(package, version=None):
    os.system(f'{PIP_EXEC} install {package}{version or ""} -qqq')


def silent_pip_uninstall(package):
    os.system(f'{PIP_EXEC} uninstall -y {package} -qqq')


def pip_uninstall(package):
    os.system(f'{PIP_EXEC} uninstall {package}')


def silent_pip_install_with_spinner(package, version=None):
    start, stop = create_spinner(f"Installing {package} {version or ''}")
    start()
    try:
        silent_pip_install_version(package, version)
    except Exception as error:
        raise error
    finally:
        stop()


def silent_pip_uninstall_with_spinner(package):
    start, stop = create_spinner(f"Removing {package}")
    start()
    try:
        silent_pip_uninstall(package)
    except Exception as error:
        raise error
    finally:
        stop()


def get_pip_installer(silent):
    if silent:
        return silent_pip_install_with_spinner
    else:
        return pip_install_version


def get_pip_uninstaller(silent):
    if silent:
        return silent_pip_uninstall_with_spinner
    else:
        return pip_uninstall
