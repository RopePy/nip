import re
import pkg_resources
from virtualenvapi.manage import VirtualEnvironment

from nip.config import paths

VERSION_NUMBERS_RE = re.compile(r'^\d+(\.\d+){2,3}$')

def is_version(string):
    return VERSION_NUMBERS_RE.match(string)


def ensure_version_is_pep_compliant(version):
    return pkg_resources.parse_version(version)


def get_version_of_venv_package(target):
    package_meta = VirtualEnvironment(paths.PYTHON_MODULES_PATH)
    package = [info_tuple[1]
               for info_tuple in package_meta.installed_packages
               if info_tuple[0].lower() == target.lower()]
    return package[0]
