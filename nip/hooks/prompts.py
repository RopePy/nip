from packaging.utils import canonicalize_name

from nip.hooks.nipfile import update_nipfile
from nip.middleware import echo_selector
from nip.utils.path import get_basename
from nip.utils.packaging import is_version


def is_default_install(ctx):
    """ Checks if `yes` option is passed to suppress prompts """
    args = ctx.obj['ARGS']
    return True if '-y' in args or '--yes' in args else False


def get_package_name(ctx, get_input=input, **kwargs):
    """ Prompts the user to input a name for their project.

    Used as a before hook. Uses the basename of the current working
    directory as a default value.

    Arguments:
        ctx {[click.Context]} -- Click application context
        **kwargs {[dict]} -- Passed kwargs

    Keyword Arguments:
        get_input {[callable]} -- Default input function (default: {input})
    """
    default_name = canonicalize_name(get_basename())
    if not is_default_install(ctx):
        default_name = get_input(
            f'Package Name ({default_name}): ') or default_name
    update_nipfile(ctx, {'name': canonicalize_name(default_name)})


def get_author(ctx, get_input=input, default_author='', **kwargs):
    """ Prompts the user for the project Authors name.

    Used as a before hook.

    Arguments:
        ctx {[click.Context]} -- Click application context
        **kwargs {[dict]} -- Passed kwargs

    Keyword Arguments:
        get_input {[callable]} -- Default input function (default: {input})
        default_author {[string]} -- Default author (default: {''})
    """
    if not is_default_install(ctx):
        default_author = get_input('Author: ') or ''
    update_nipfile(ctx, {'author': default_author})


def get_version(ctx, get_input=input, default_version='0.1.0', **kwargs):
    """ Prompts the user to input a version for their project.

    Used as a before hook. Input is validated. Upon failure
    it recursively calls itself to prompt the user for a valid
    version.

    Arguments:
        ctx {[click.Context]} -- Click application context
        **kwargs {[dict]} -- Passed kwargs

    Keyword Arguments:
        get_input {[callable]} -- Default input function (default: {input})
        default_version {[string]} -- Default version (default: {'0.1.0'})
    """

    echo = echo_selector(ctx)
    if is_default_install(ctx):
        return update_nipfile(ctx, {'version': default_version})
    version = get_input(f'Version ({default_version}): ') or default_version
    if not is_version(version):
        echo('Not a valid version number.')
        get_version(ctx, get_input=input, **kwargs)
    else:
        update_nipfile(ctx, {'version': version})


def get_license(ctx, get_input=input, default_license='MIT', **kwargs):
    """ Prompts the user to input a License for their project.

    Used as a before hook.

    Arguments:
        ctx {[click.Context]} -- Click application context
        **kwargs {[dict]} -- Passed kwargs

    Keyword Arguments:
        get_input {[callable]} -- Default input function (default: {input})
        default_license {[string]} -- Default license (default: {'MIT'})
    """
    if not is_default_install(ctx):
        default_license = get_input(
            f'License ({default_license}): ')
    update_nipfile(ctx, {'license': default_license})
