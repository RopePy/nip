from nip.providers.python import call_python_command_from_venv
from nip.hooks.nipfile import exit_if_no_nipfile, parse_command
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
    final_command = parse_command(ctx, command)
    call_python_command_from_venv(final_command)

__all__ = ['nip_run', 'HOOKS']
