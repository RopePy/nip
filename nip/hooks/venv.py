from nip.middleware import echo_selector, env_selector
from nip.providers.virtualenv import create_venv
from nip.utils.path import directory_is_empty, get_python_modules_path


def create_venv_if_none_exists(ctx, *args, **kwargs):
    """ Creates a virtual environment in the `cwd`.

    If one already exists, this hook does nothing.

    Usually used as an after hook.

    Arguments:
        ctx {[click.Context]} -- Click application context
        *args {[list]} -- Passed args
        **kwargs {[dict]} -- Passed kwargs

    """
    env = env_selector(ctx)
    if directory_is_empty(get_python_modules_path(env)):
        echo = echo_selector(ctx)
        echo(f'Creating `{env.PYTHON_MODULES}` directory .. ')
        create_venv(env)
