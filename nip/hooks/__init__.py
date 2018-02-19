from functools import wraps

from nip.hooks.gitignore import create_gitignore_for_project
from nip.hooks.logger import logger
from nip.hooks.messages import (
    create_command_greeting,
    print_success_message)
from nip.hooks.nipfile import (
    exit_if_current_dir_is_not_empty,
    exit_if_nipfile,
    exit_if_no_nipfile,
    save_nipfile,
    write_nipfile)
from nip.hooks.prompts import (
    get_author,
    get_basename,
    get_license,
    get_package_name,
    get_version)
from nip.hooks.requirements import write_requirements_file
from nip.hooks.setup import write_setup_file
from nip.hooks.venv import create_venv_if_none_exists


def execute_hooks(hooks, ctx, *args, **kwds):
    for hook in hooks:
        hook(ctx, *args, **kwds)


def apply_hooks(hooks):
    """ Wraps a function in a hook block """
    def outer(func):
        @wraps(func)
        def wrapper(ctx, *args, **kwds):
            try:
                execute_hooks(hooks['before'], ctx, *args, **kwds)
                try:
                    func(ctx, *args, **kwds)
                except Exception as error:
                    execute_hooks(hooks['error'], ctx, error, *args, **kwds)
                else:
                    execute_hooks(hooks['after'], ctx, *args, **kwds)
            except Exception as hook_error:
                print('nip encountered a problem and had to quit.')
                raise hook_error
        return wrapper
    return outer


__all__ = [
    'apply_hooks',
    'get_hooks',
    'create_venv_if_none_exists',
    'create_command_greeting',
    'print_success_message',
    'exit_if_current_dir_is_not_empty',
    'exit_if_nipfile',
    'exit_if_no_nipfile',
    'get_author',
    'get_basename',
    'get_license',
    'get_package_name',
    'get_version',
    'write_requirements_file',
    'write_setup_file',
    'create_gitignore_for_project',
    'save_nipfile',
    'write_nipfile',
    'logger',
]
