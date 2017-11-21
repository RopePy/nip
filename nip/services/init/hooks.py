from nip.nip import create_nipfile
from nip.providers.python import create_venv
from nip.middleware.nipfile import nipfile_selector
from nip.hooks.nipfile import exit_if_current_dir_is_not_empty
from nip.hooks.freeze import nip_freeze
from nip.hooks.messages import create_command_greeting, default_success_message
from nip.hooks.prompts import get_author, get_license, get_package_name
from nip.hooks.logger import logger
from nip.utils.gitignore import create_nipfile_gitignore
from nip.utils.spinner import create_spinner

start_spinner, stop_spinner = create_spinner('Initialising..')


HOOKS = dict(
    before=[
        create_command_greeting('Init'),
        exit_if_current_dir_is_not_empty,
        get_package_name,
        get_author,
        get_license,
        start_spinner
    ],
    after=[
        nip_freeze,
        stop_spinner,
        default_success_message
    ],
    error=[
        stop_spinner,
        logger
    ],
)


def nip_init(ctx):
    nipfile_options = nipfile_selector(ctx)
    create_venv()
    create_nipfile(nipfile_options)
    create_nipfile_gitignore()


__all__ = ['nip_init', 'HOOKS']
