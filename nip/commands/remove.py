from nip.nip import remove_dep_from_nipfile_context
from nip.providers.pip import get_pip_uninstaller
from nip.middleware.nipfile import nipfile_selector
from nip.hooks import (exit_if_no_nipfile, write_requirements_file,
                       create_command_greeting, print_success_message,
                       logger)


HOOKS = dict(
    before=[
        create_command_greeting('Remove'),
        exit_if_no_nipfile,
    ],
    after=[
        write_requirements_file,
        print_success_message
    ],
    error=[logger],
)


def nip_remove(ctx, package, silent=True):
    nipfile = nipfile_selector(ctx)
    pip_uninstall = get_pip_uninstaller(silent)
    pip_uninstall(package)
    remove_dep_from_nipfile_context(package, nipfile)


__all__ = ['nip_remove', 'HOOKS']
