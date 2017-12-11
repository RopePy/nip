from nip.hooks.nipfile import update_nipfile
from nip.middleware.echo import echo_selector
from nip.utils.path import get_basename
from nip.utils.regex import is_version


def get_package_name(ctx, get_input=input, **kwargs):
    default = get_basename()
    package_name = get_input(f'Package Name ({default}): ') or default
    update_nipfile(ctx, {'name': package_name})


def get_author(ctx, get_input=input, **kwargs):
    authors_name = get_input('Author: ')
    update_nipfile(ctx, {'author': authors_name})


def get_version(ctx, get_input=input, **kwargs):
    echo = echo_selector(ctx)
    version = get_input('Version (0.1.0): ') or '0.1.0'
    if not is_version(version):
        echo('Not a valid version number.')
        get_version(ctx, get_input=input, **kwargs)
    else:
        update_nipfile(ctx, {'version': version})


def get_license(ctx, get_input=input, **kwargs):
    software_license = get_input('License (MIT): ') or 'MIT'
    update_nipfile(ctx, {'license': software_license})
