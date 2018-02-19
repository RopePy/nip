from nip.providers.git import create_gitignore
from nip.middleware import env_selector


def create_gitignore_for_project(ctx, *args, **kw):
    env = env_selector(ctx)
    create_gitignore(env)
