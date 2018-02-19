import time
import nip
from nip.middleware.echo import echo_selector


def create_command_greeting(command_name, extra=None):
    """ Prints the main cli greeting """
    def hook(ctx, *args, **kwargs):
        echo = echo_selector(ctx)
        echo(f'{nip.package_name} - v{nip.package_version} - '
             f'{command_name} - {extra or ""}'
             f'Made with Love, by Duroktar © 2017 - {time.gmtime().tm_year}\n')
    return hook


def print_success_message(ctx, *args, **kwargs):
    """ The default success message """
    echo = echo_selector(ctx)
    echo(f'Finished.')
