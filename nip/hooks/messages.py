import nip
from time import gmtime
from nip.middleware.echo import echo_selector


def create_command_greeting(command_name, extra=None):
    def wrapper(ctx, *args, **kwargs):
        echo = echo_selector(ctx)
        echo(f'{nip.package_name} - v{nip.package_version} - '
             f'{command_name} - {extra or ""}'
             f'Made with Love, by Duroktar © {gmtime().tm_year}\n')
    return wrapper


def default_success_message(ctx, *args, **kwargs):
    echo = echo_selector(ctx)
    echo(f'Finished.')
