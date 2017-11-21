from nip.nip import install_dependancies
from nip.middleware.nipfile import nipfile_selector
from nip.hooks.nipfile import exit_if_no_nipfile
from nip.hooks.freeze import nip_freeze
from nip.hooks.venv import create_venv_if_none_exists
from nip.hooks.messages import create_command_greeting, default_success_message
from nip.hooks.logger import logger


HOOKS = dict(
    before=[
        create_command_greeting('Install'),
        exit_if_no_nipfile,
        create_venv_if_none_exists,
    ],
    after=[nip_freeze, default_success_message],
    error=[logger],
)


def nip_install(ctx, prod, silent=True):
    nipfile = nipfile_selector(ctx)
    dependencies = nipfile.get('dependencies')
    if not prod:
        dependencies = {**dependencies, **(nipfile.get('dev_dependencies'))}

    install_dependancies(dependencies, silent)


__all__ = ['nip_install', 'HOOKS']
