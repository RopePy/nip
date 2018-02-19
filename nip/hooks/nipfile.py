from nip.nip import nipfile_exists, write_nipfile
from nip.middleware import nipfile_selector, echo_selector
from nip.utils.path import current_working_directory_is_empty


def update_nipfile(ctx, payload, *args, **kw):
    ctx.obj['NIPFILE'] = {**nipfile_selector(ctx), **payload}


def save_nipfile(ctx, *args, **kw):
    nipfile_options = nipfile_selector(ctx)
    write_nipfile(nipfile_options)


def exit_if_no_nipfile(ctx, *args, **kwargs):
    echo = echo_selector(ctx)
    if not nipfile_exists():
        echo('No nipfile found. Aborting.')
        exit(1)


def exit_if_nipfile(ctx, *args, **kwargs):
    echo = echo_selector(ctx)
    if nipfile_exists():
        echo('Found existing nipfile. Aborting.')
        exit(1)


def exit_if_current_dir_is_not_empty(ctx, *args, **kwargs):
    echo = echo_selector(ctx)
    if not current_working_directory_is_empty():
        echo('Working directory is not empty. Aborting.')
        exit(1)
