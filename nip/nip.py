import os
import json
from nip.config import paths
from nip.providers.pip import get_pip_installer
from nip.utils.formatting import pformat_json
from nip.utils.regex import is_version


__all__ = [
    'nip_file_exists',
    'create_nipfile',
    'load_nipfile',
    'get_version_from_settings',
    'get_existing_nipfile_or_create_new',
    'add_dep_to_nipfile_context',
    'remove_dep_from_nipfile_context',
    'write_nipfile',
]


DEFAULT_NIPFILE_OPTIONS = dict(
    name='',
    author=''
)


DEFAULT_VERSION_OPTIONS = dict(
    latest=''
)


def nip_file_exists():
    return os.path.exists(paths.NIPFILE_PATH)


def create_nipfile(options, path=paths.NIPFILE_PATH):
    with open(path, 'w') as f:
        json.dump(options, f, indent=4)


def load_nipfile():
    if not nip_file_exists():
        return {}
    with open(paths.NIPFILE_PATH, 'r') as f:
        return json.load(f)


def get_existing_nipfile_or_create_new():
    return {**DEFAULT_NIPFILE_OPTIONS, **load_nipfile()}


def get_nipfile_scripts():
    if not nip_file_exists():
        return
    nipfile = load_nipfile()
    scripts = nipfile.get('scripts')
    if not scripts:
        return
    commands = scripts.keys()
    print(commands)
    return commands


def get_version_from_settings(version):
    return DEFAULT_VERSION_OPTIONS.get(version, '')


def add_dep_to_nipfile_context(dep, nipfile, dev=False):
    dependency_key = 'dev_dependencies' if dev else 'dependencies'
    try:
        nipfile[dependency_key].update({**dep})
    except KeyError:
        nipfile[dependency_key] = dict()
        return add_dep_to_nipfile_context(dep, nipfile, dev)
    else:
        return nipfile


def remove_dep_from_nipfile_context(dep, nipfile):
    for key in ['dev_dependencies', 'dependencies']:
        nipfile.get(key, {}).pop(dep, None)
    return write_nipfile(nipfile)


def write_nipfile(nipfile):
    try:
        with open(paths.NIPFILE_PATH, 'w') as f:
            formatted_nipfile = pformat_json(nipfile)
            return f.write(formatted_nipfile)
    except FileNotFoundError:
        exit(1)


def install_dependancies(dependencies, silent):
    pip_installer = get_pip_installer(silent)
    for package, version in dependencies.items():
        validated_version = validate_version(version)
        pip_installer(package, validated_version)


def validate_version(version):
    if not is_version(version):
        return get_version_from_settings(version)
    else:
        return version


def nipfile_setter(ctx, payload):
    ctx.obj['NIPFILE'] = payload
