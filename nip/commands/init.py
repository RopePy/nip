from nip.providers.virtualenv import create_venv
from nip.middleware import env_selector
from nip.hooks import (
    create_command_greeting, print_success_message, get_package_name,
    get_author, get_version, get_license, create_gitignore_for_project, logger,
    write_setup_file, write_requirements_file,
    exit_if_current_dir_is_not_empty, save_nipfile
)
from nip.utils.spinner import create_spinner

# This kinda goes wonky in debug mode ..
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
        print_success_message
    ],
    error=[
        stop_spinner,
        logger
    ],
)


def nip_init(ctx, yes=False):
    """ Init is pretty simple, creates a venv ...
        Everything else is done with hooks. """
    env = env_selector(ctx)
    create_venv(env)


__all__ = ['nip_init', 'HOOKS']
