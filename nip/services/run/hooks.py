from nip.api.python import call_command_from_venv
from nip.hooks.nipfile import exit_if_no_nipfile, get_nip_script
from nip.hooks.messages import create_command_greeting
from nip.hooks.logger import logger

HOOKS = dict(
    before=[
        create_command_greeting('Run'),
        exit_if_no_nipfile,
    ],
    after=[],
    error=[logger],
)


def nip_run(ctx, command):
    command = get_nip_script(ctx, command)
    return call_command_from_venv(command)


__all__ = ['nip_run', 'HOOKS']
