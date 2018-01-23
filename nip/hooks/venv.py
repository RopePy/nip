from nip.middleware.echo import echo_selector
from nip.providers.python import create_venv
from nip.utils.path import current_working_directory_has_venv


def create_venv_if_none_exists(ctx, *args, **kwargs):
    if not current_working_directory_has_venv():
        echo = echo_selector(ctx)
        echo('Creating `python_modules` directory.')
        create_venv()
