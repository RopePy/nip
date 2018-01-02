from nip.nip import nip_file_exists, write_nipfile

from nip.middleware.nipfile import (nipfile_selector, scripts_selector)
from nip.middleware.echo import echo_selector
from nip.utils.path import current_working_directory_is_empty


def exit_if_no_nipfile(ctx, *args, **kwargs):
    echo = echo_selector(ctx)
    if not nip_file_exists():
        echo('No nipfile found. Aborting.')
        exit(1)


def exit_if_nipfile_exists(ctx, *args, **kwargs):
    echo = echo_selector(ctx)
    if nip_file_exists():
        echo('Found existing nipfile. Aborting.')
        exit(1)


def exit_if_current_dir_is_not_empty(ctx, *args, **kwargs):
    echo = echo_selector(ctx)
    if not current_working_directory_is_empty():
        echo('Working directory is not empty. Aborting.')
        exit(1)


def update_nipfile_context(ctx, payload, *args, **kw):
    ctx.obj['NIPFILE'] = {**nipfile_selector(ctx), **payload}


def save_nipfile(ctx, *args, **kw):
    nipfile_options = nipfile_selector(ctx)
    write_nipfile(nipfile_options)


def get_nip_script(ctx, command, *args, **kw):
    echo = echo_selector(ctx)
    scripts = scripts_selector(ctx)
    final_command = scripts.get(command)
    if not final_command:
        echo('No command was provided. Exiting..')
        exit(1)
    return final_command
