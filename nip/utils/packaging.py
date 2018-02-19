import os
import re
import pkg_resources

from packaging.requirements import Requirement
from virtualenvapi.manage import VirtualEnvironment

from nip.config import defaults
from nip.nip import get_version_tag
from nip.utils.path import get_python_modules_path


VERSION_NUMBERS_RE = re.compile(r'^\d+(\.\d+){2,3}$')


def get_package_meta(package):
    dep = Requirement(package)
    specs = [f"{spec.operator}{spec.version}" for spec in dep.specifier]
    version_spec = ",".join(specs)
    return dep.name, version_spec


def get_version_of_venv_package(target, env=defaults):
    py_modules_path = get_python_modules_path(env)
    package_meta = VirtualEnvironment(os.path.abspath(py_modules_path))
    package = [info_tuple[1]
               for info_tuple in package_meta.installed_packages
               if info_tuple[0].lower() == target.lower()]
    return package and package[0]


def is_version(string):
    return True if VERSION_NUMBERS_RE.match(string) else False


def is_pinned_version(string):
    is_tag = bool(string == 'latest')
    is_valid = bool(string.startswith('~=') and is_version(string[2:]))
    if is_tag or is_valid:
        return True
    else:
        return False


def parse_version_string(version):
    return pkg_resources.parse_version(version)


def validate_version(version):
    if not is_version(version):
        return get_version_tag(version)
    else:
        return version
