import click

from nip import commands
from nip.hooks import apply_hooks
from nip.middleware import (
    register_nipfile,
    register_echo,
    register_env)
from nip.utils.click import DefaultGroup


@click.group(cls=DefaultGroup,
             default_command='run',
             noargs_command='install')
@click.pass_context
def cli(ctx):
    """ NIP - nip isn't pip """
    register_env(ctx, overrides={})
    register_echo(ctx, echo=click.echo)
    register_nipfile(ctx)


@cli.command()
@click.option('--yes', '-y', is_flag=True, default=False,
              help="Accept nip defaults and generate new project."
                   "(answers yes to all default questions)")
@click.pass_context
@apply_hooks(commands.init.HOOKS)
def init(ctx, yes):
    """ Generates a new Python project in the current folder. """
    commands.init.nip_init(ctx, yes)


@cli.command()
@click.option('--prod', '-P', is_flag=True, default=False,
              help="Install package in production mode."
                   "(ignores packages in dev_dependencies)")
@click.pass_context
@apply_hooks(commands.install.HOOKS)
def install(ctx, prod):
    """ Install all project dependencies and initialize a new
        venv if necessary. """
    commands.install.nip_install(ctx, prod)


@cli.command()
@click.argument('script_name', nargs=-1)
@click.pass_context
@apply_hooks(commands.run.HOOKS)
def run(ctx, script_name):
    """ Run a script from the nipfile. """
    commands.run.nip_run(ctx, script_name)


@cli.command()
@click.argument('packages', nargs=-1)
@click.option('--dev', '-D', is_flag=True, default=False,
              help="Install package as a dev-dependency.")
@click.pass_context
@apply_hooks(commands.add.HOOKS)
def add(ctx, packages, dev):
    """ Install a new project dependency and add to nipfile. """
    commands.add.nip_add(ctx, packages, dev)


@cli.command()
@click.argument('package')
@click.pass_context
@apply_hooks(commands.remove.HOOKS)
def remove(ctx, package):
    """ Remove a dependency from your project. """
    commands.remove.nip_remove(ctx, package)


def main():
    cli(obj={})


if __name__ == '__main__':
    cli(obj={})
