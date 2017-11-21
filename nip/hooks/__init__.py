from functools import wraps


HOOKS = dict(
    before=[],
    after=[],
    error=[],
)


def execute_hooks(hooks, ctx, *args, **kwds):
    for hook in hooks:
        hook(ctx, *args, **kwds)


def apply_hooks(hooks):
    def outer(func):
        @wraps(func)
        def wrapper(ctx, *args, **kwds):
            execute_hooks(hooks['before'], ctx, *args, **kwds)
            try:
                func(ctx, *args, **kwds)
            except Exception as error:
                execute_hooks(hooks['error'], ctx, error, *args, **kwds)
            else:
                execute_hooks(hooks['after'], ctx, *args, **kwds)
        return wrapper
    return outer


def get_hooks():
    return HOOKS


__all__ = ['apply_hooks', 'get_hooks']
