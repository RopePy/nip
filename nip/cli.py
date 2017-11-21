import click
import nip.services as services

from nip.hooks import apply_hooks
from nip.middleware import register_hooks, register_nipfile, register_echo


@click.group()
@click.pass_context
def cli(ctx):
    """NIP - nip isn't pip"""
    register_echo(ctx, echo=click.echo)
    register_nipfile(ctx)
    register_hooks(ctx)


@cli.command()
@click.pass_context
@apply_hooks(services.init.HOOKS)
def init(ctx):
    """ Not a bit like pip init """
    services.init.nip_init(ctx)


@cli.command()
@click.option('--prod', '-P', is_flag=True, default=False)
@click.pass_context
@apply_hooks(services.install.HOOKS)
def install(ctx, prod):
    """ This ain't at all like the old pip install """
    services.install.nip_install(ctx, prod)


@cli.command()
@click.argument('command')
@click.pass_context
@apply_hooks(services.run.HOOKS)
def run(ctx, command):
    """ Python is fun and so is nip run """
    services.run.nip_run(ctx, command)


@cli.command()
@click.argument('package')
@click.option('--version', default="latest")
@click.option('--dev', '-D', is_flag=True, default=False)
@click.pass_context
@apply_hooks(services.add.HOOKS)
def add(ctx, package, version, dev):
    """ Pip isn't bad and neither's nip add """
    services.add.nip_add(ctx, package, version, dev)


@cli.command()
@click.argument('package')
@click.pass_context
@apply_hooks(services.remove.HOOKS)
def remove(ctx, package):
    """ Yeah, this one just removes packages .. """
    services.remove.nip_remove(ctx, package)

def main():
    cli(obj={})

if __name__ == '__main__':
    cli(obj={})
