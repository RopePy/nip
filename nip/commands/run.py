from nip.providers.virtualenv import call_command_from_venv
from nip.middleware import scripts_selector, echo_selector, env_selector
from nip.hooks import (
    exit_if_no_nipfile, create_command_greeting, logger)


HOOKS = dict(
    before=[
        create_command_greeting('Run'),
        exit_if_no_nipfile,
    ],
    after=[],
    error=[logger],
)


def nip_run(ctx, cmd_args):
    scripts = scripts_selector(ctx)
    env = env_selector(ctx)
    script_name, *args = cmd_args
    command = scripts.get(script_name)
    if command is None:
        echo = echo_selector(ctx)
        echo('Command not found. Exiting..')
        exit(1)

    command_string = ' '.join([command, *args])
    return call_command_from_venv(command_string, env=env)


__all__ = ['nip_run', 'HOOKS']
