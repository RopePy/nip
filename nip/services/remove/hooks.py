from nip.nip import remove_dep_from_nipfile_context
from nip.api.pip import get_pip_uninstaller
from nip.middleware.nipfile import nipfile_selector
from nip.hooks.nipfile import exit_if_no_nipfile
from nip.hooks.requirements import write_requirements_file
from nip.hooks.messages import create_command_greeting, default_success_message
from nip.hooks.logger import logger


HOOKS = dict(
    before=[
        create_command_greeting('Remove'),
        exit_if_no_nipfile,
    ],
    after=[write_requirements_file, default_success_message],
    error=[logger],
)


def nip_remove(ctx, package, silent=True):
    nipfile = nipfile_selector(ctx)
    pip_uninstall = get_pip_uninstaller(silent)
    pip_uninstall(package)
    remove_dep_from_nipfile_context(package, nipfile)


__all__ = ['nip_remove', 'HOOKS']
