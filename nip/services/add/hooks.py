from nip.nip import write_nipfile, add_dep_to_nipfile_context
from nip.middleware.nipfile import nipfile_selector
from nip.providers.pip import get_pip_installer
from nip.hooks.nipfile import exit_if_no_nipfile
from nip.hooks.freeze import nip_freeze
from nip.hooks.messages import create_command_greeting, default_success_message
from nip.hooks.logger import logger


HOOKS = dict(
    before=[
        create_command_greeting('Add'),
        exit_if_no_nipfile,
    ],
    after=[nip_freeze, default_success_message],
    error=[logger],
)


def nip_add(ctx, package, version='latest', dev=False, silent=True):
    nipfile_options = nipfile_selector(ctx)
    pip_installer = get_pip_installer(silent)
    pip_installer(package)
    add_dep_to_nipfile_context({package: version}, nipfile_options, dev)
    write_nipfile(nipfile_options)


__all__ = ['nip_add', 'HOOKS']
