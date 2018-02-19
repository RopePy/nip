from nip.config import defaults
from nip.utils.decorators import create_spinner_with_message
from nip.utils.packaging import (
    validate_version,
    get_package_meta,
    get_version_of_venv_package)
from nip.providers.virtualenv import call_command_from_venv


def pip_install(package, version="", env=defaults):
    call_command_from_venv(f'{env.PIP} install {package}{version or ""} -qqq')


def pip_uninstall(package, env=defaults):
    call_command_from_venv(f'{env.PIP} uninstall {package} -qqq')


def pip_install_with_spinner(package, version="", env=defaults):
    wrapper = create_spinner_with_message(f"Installing {package} {version}")

    def installer(*args, **kw):
        return pip_install(*args, **kw, env=env)
    wrapper(installer)(package, version)


def pip_uninstall_with_spinner(package, env=defaults):
    wrapper = create_spinner_with_message(f"Removing {package}")

    def uninstaller(*args, **kw):
        return pip_uninstall(*args, **kw, env=env)
    wrapper(uninstaller)(package)


def get_pip_installer(spinner):
    if spinner:
        return pip_install_with_spinner
    else:
        return pip_install


def get_pip_uninstaller(spinner):
    if spinner:
        return pip_uninstall_with_spinner
    else:
        return pip_uninstall


def pip_install_dependancies(dependencies, spinner, env=defaults):
    pip_installer = get_pip_installer(spinner)
    for package, version in dependencies.items():
        validated_version = validate_version(version)
        pip_installer(package, validated_version, env=env)


def pip_install_and_return_meta(package, spinner, env=defaults):
    name, version_spec = get_package_meta(package)
    pip_installer = get_pip_installer(spinner)
    pip_installer(name, version_spec, env=env)
    if not version_spec:
        version_spec = get_version_of_venv_package(name, env)
    return name, version_spec
