from nip.hooks import get_hooks

def register_hooks(ctx):
    ctx.obj['HOOKS'] = get_hooks()

hooks_selector = lambda ctx: ctx.obj['HOOKS']

__all__ = ['register_hooks', 'hooks_selector']
