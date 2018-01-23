from nip.providers.python import create_venv
from nip.hooks.nipfile import exit_if_current_dir_is_not_empty, save_nipfile
from nip.hooks.requirements import write_requirements_file
from nip.hooks.setup import write_setup_file
from nip.hooks.messages import create_command_greeting, default_success_message
from nip.hooks.prompts import (
    get_author, get_license, get_package_name, get_version)
from nip.hooks.git import create_gitignore_for_project
from nip.hooks.logger import logger
from nip.utils.spinner import create_spinner

start_spinner, stop_spinner = create_spinner('Initialising..')

HOOKS = dict(
    before=[
        create_command_greeting('Init'),
        exit_if_current_dir_is_not_empty,
        get_package_name,
        get_author,
        get_version,
        get_license,
        start_spinner
    ],
    after=[
        save_nipfile,
        write_setup_file,
        write_requirements_file,
        create_gitignore_for_project,
        stop_spinner,
        default_success_message
    ],
    error=[
        stop_spinner,
        logger
    ],
)


def nip_init(ctx):
    create_venv()


__all__ = ['nip_init', 'HOOKS']
