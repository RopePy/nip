from nip.config import defaults
from nip.utils.decorators import make_dot_accessible


def register_env(ctx, overrides={}):
    env = {
        'PIP': defaults.PIP,
        'PYTHON': defaults.PYTHON,
        'GITIGNORE': defaults.GITIGNORE,
        'PYTHON_SETUP_PY': defaults.PYTHON_SETUP_PY,
        'PYTHON_MODULES': defaults.PYTHON_MODULES,
        'REQUIREMENTS_FILE': defaults.REQUIREMENTS_FILE,
        'DEV_REQUIREMENTS_FILE': defaults.DEV_REQUIREMENTS_FILE
    }

    # By making the ENV accessible by "dot", it means we can do this
    # `ctx.obj['ENV'].PIP`. Which makes it compatible with using an
    # imported python file filled with globals as a fallback without
    # having to change any existing semantics. (A little sorcery can
    # hide a lot of sin..)
    ctx.obj['ENV'] = make_dot_accessible({**env, **overrides})


def env_selector(ctx):
    return ctx.obj['ENV']
