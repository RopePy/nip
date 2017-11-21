from nip.nip import nip_file_exists
from nip.middleware.nipfile import nipfile_selector
from nip.utils.path import current_working_directory_is_empty


def exit_if_no_nipfile(ctx, *args, echo=print, **kwargs):
    if not nip_file_exists():
        echo('No nipfile found. Aborting.')
        exit(1)


def exit_if_nipfile_exists(ctx, *args, echo=print, **kwargs):
    if nip_file_exists():
        echo('Found existing nipfile. Aborting.')
        exit(1)


def exit_if_current_dir_is_not_empty(ctx, *args, echo=print, **kwargs):
    if not current_working_directory_is_empty():
        echo('Working directory is not empty. Aborting.')
        exit(1)


def update_nipfile(ctx, payload):
    ctx.obj['NIPFILE'] = {**nipfile_selector(ctx), **payload}


def parse_command(ctx, command):
    scripts = ctx.obj['NIPFILE'].get('scripts', None)
    if scripts is None:
        exit(1)
    final_command = scripts.get(command, None)
    if final_command is None:
        exit(1)
    return final_command


__all__ = [
    'nipfile_selector',
    'exit_if_nipfile_exists',
    'exit_if_no_nipfile',
    'exit_if_current_dir_is_not_empty',
    'update_nipfile',
    'parse_command',
]
