from nip.hooks.nipfile import update_nipfile_context
from nip.middleware.echo import echo_selector
from nip.utils.path import get_basename
from nip.utils.version import is_version
from packaging.utils import canonicalize_name


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

    default = canonicalize_name(get_basename())
    package_name = get_input(f'Package Name ({default}): ') or default
    update_nipfile_context(ctx, {'name': canonicalize_name(package_name)})


def get_author(ctx, get_input=input, **kwargs):
    """ Prompts the user for the project Authors name.

    Used as a before hook.

    Arguments:
        ctx {[click.Context]} -- Click application context
        **kwargs {[dict]} -- Passed kwargs

    Keyword Arguments:
        get_input {[callable]} -- Default input function (default: {input})
    """

    authors_name = get_input('Author: ')
    update_nipfile_context(ctx, {'author': authors_name})


def get_version(ctx, get_input=input, **kwargs):
    """ Prompts the user to input a version for their project.

    Used as a before hook. Input is validated. Upon failure
    it recursively calls itself to prompt the user for a valid
    version.

    Arguments:
        ctx {[click.Context]} -- Click application context
        **kwargs {[dict]} -- Passed kwargs

    Keyword Arguments:
        get_input {[callable]} -- Default input function (default: {input})
    """

    echo = echo_selector(ctx)
    version = get_input('Version (0.1.0): ') or '0.1.0'
    if not is_version(version):
        echo('Not a valid version number.')
        get_version(ctx, get_input=input, **kwargs)
    else:
        update_nipfile_context(ctx, {'version': version})


def get_license(ctx, get_input=input, **kwargs):
    """ Prompts the user to input a License for their project.

    Used as a before hook.

    Arguments:
        ctx {[click.Context]} -- Click application context
        **kwargs {[dict]} -- Passed kwargs

    Keyword Arguments:
        get_input {[callable]} -- Default input function (default: {input})
    """

    software_license = get_input('License (MIT): ') or 'MIT'
    update_nipfile_context(ctx, {'license': software_license})
