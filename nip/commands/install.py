from nip.providers.pip import pip_install_dependancies
from nip.middleware import nipfile_selector, env_selector
from nip.hooks import (exit_if_no_nipfile, write_requirements_file,
                       create_venv_if_none_exists, create_command_greeting,
                       print_success_message, logger)


HOOKS = dict(
    before=[
        create_command_greeting('Install'),
        exit_if_no_nipfile,
        create_venv_if_none_exists,
    ],
    after=[
        write_requirements_file,
        print_success_message
    ],
    error=[logger],
)


def nip_install(ctx, production, silent=True):
    nipfile = nipfile_selector(ctx)
    env = env_selector(ctx)
    deps = nipfile.get('dependencies', {})
    if not production:
        deps = {**deps, **(nipfile.get('dev_dependencies', {}))}
    pip_install_dependancies(deps, silent, env)


__all__ = ['nip_install', 'HOOKS']
