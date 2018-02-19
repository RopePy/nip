import os
import json

from nip.utils.formatting import pformat_json
from nip.utils.path import get_nipfile_path


DEFAULT_NIPFILE_OPTIONS = {
    "name": '',
    "author": ''
}


DEFAULT_VERSION_OPTIONS = {
    "latest": ''   # let pip handle resolving the latest version
}


def create_nipfile(options, path=get_nipfile_path()):
    with open(path, 'w') as f:
        json.dump(options, f, indent=4)


def load_nipfile():
    if not nipfile_exists():
        return {}
    with open(get_nipfile_path(), 'r') as f:
        return json.load(f)


def get_existing_nipfile_or_create_new():
    return {**DEFAULT_NIPFILE_OPTIONS, **load_nipfile()}


def nipfile_exists():
    return os.path.exists(get_nipfile_path())


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

    # FIXME: this side effect should not be here ...
    # The actual file writing would be done from an after hook
    return write_nipfile(nipfile)


def get_version_tag(version):
    return DEFAULT_VERSION_OPTIONS.get(version, '')


def write_nipfile(nipfile):
    try:
        with open(get_nipfile_path(), 'w') as f:
            formatted_nipfile = pformat_json(nipfile)
            return f.write(formatted_nipfile + '\n')
    except FileNotFoundError:
        exit(1)
