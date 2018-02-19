from nip.nip import add_dep_to_nipfile_context
from nip.middleware import nipfile_selector, echo_selector, env_selector
from nip.hooks import (exit_if_no_nipfile, save_nipfile,
                       write_requirements_file,
                       create_command_greeting, print_success_message,
                       logger)
from nip.providers.pip import pip_install_and_return_meta


HOOKS = dict(
    before=[
        create_command_greeting('Add'),
        exit_if_no_nipfile,
    ],
    after=[
        save_nipfile,
        write_requirements_file,
        print_success_message
    ],
    error=[logger],
)


def nip_add(ctx, packages, dev=False, silent=True):
    nipfile = nipfile_selector(ctx)
    echo = echo_selector(ctx)
    env = env_selector(ctx)
    dev_mode = "dev-" if dev else ""
    echo(f"Installing {dev_mode}dependencies - {', '.join(packages)}")

    for package in packages:
        name, version = pip_install_and_return_meta(package, silent, env)
        add_dep_to_nipfile_context(
            {name: f"{'~=' + version if version else ''}"}, nipfile, dev)


__all__ = ['nip_add', 'HOOKS']
