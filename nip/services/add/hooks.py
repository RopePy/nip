from nip.nip import add_dep_to_nipfile_context
from nip.middleware.nipfile import nipfile_selector
from nip.middleware.echo import echo_selector
from nip.providers.pip import pip_install_and_return_meta
from nip.hooks.nipfile import exit_if_no_nipfile, save_nipfile
from nip.hooks.requirements import write_requirements_file
from nip.hooks.messages import create_command_greeting, default_success_message
from nip.hooks.logger import logger


HOOKS = dict(
    before=[
        create_command_greeting('Add'),
        exit_if_no_nipfile,
    ],
    after=[
        save_nipfile,
        write_requirements_file,
        default_success_message
    ],
    error=[logger],
)


def nip_add(ctx, packages, dev=False, silent=True):
    nipfile = nipfile_selector(ctx)
    echo = echo_selector(ctx)
    echo(f"Installing dependencies - {', '.join(packages)}")

    for package in packages:
        name, version = pip_install_and_return_meta(package, silent)
        add_dep_to_nipfile_context({name: f"~={version}"}, nipfile, dev)


__all__ = ['nip_add', 'HOOKS']
