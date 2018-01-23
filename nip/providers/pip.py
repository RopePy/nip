import os
from nip.config.paths import PYTHON_MODULES_PIP_EXEC
from nip.utils.decorators import create_spinner_with_message
from nip.utils.version import get_version_of_venv_package

from packaging.requirements import Requirement

__all__ = ['pip_install', 'pip_install_version', 'pip_uninstall']


def pip_install(package, pip=PYTHON_MODULES_PIP_EXEC):
    return pip_install_version(package, version=None, pip=pip)


def pip_install_version(package, version="", pip=PYTHON_MODULES_PIP_EXEC):
    os.system(f'{pip} install {package}{version}')


def silent_pip_install(package, version="", pip=PYTHON_MODULES_PIP_EXEC):
    os.system(f'{pip} install {package}{version} -qqq')


def silent_pip_uninstall(package, pip=PYTHON_MODULES_PIP_EXEC):
    os.system(f'{pip} uninstall -y {package} -qqq')


def pip_uninstall(package, pip=PYTHON_MODULES_PIP_EXEC):
    os.system(f'{pip} uninstall {package}')


def silent_pip_install_with_spinner(package, version=""):
    wrapper = create_spinner_with_message(f"Installing {package} {version}")
    wrapper(silent_pip_install)(package, version)


def silent_pip_uninstall_with_spinner(package):
    wrapper = create_spinner_with_message(f"Removing {package}")
    wrapper(silent_pip_uninstall)(package)


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


def parse_package_meta(package):
    dep = Requirement(package)
    specs = [f"{spec.operator}{spec.version}" for spec in dep.specifier]
    version_spec = ",".join(specs)
    return dep.name, version_spec


def pip_install_and_return_meta(package, silent):
    name, version_spec = parse_package_meta(package)
    pip_installer = get_pip_installer(silent)
    pip_installer(name, version_spec)

    # We can wait till after install here (that, or parse the pip cli output)
    if not version_spec:
        version_spec = get_version_of_venv_package(name)
    return name, version_spec
