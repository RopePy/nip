from nip.middleware.nipfile import register_nipfile
from nip.middleware.hooks import register_hooks
from nip.middleware.echo import register_echo

__all__ = ['register_nipfile', 'register_hooks', 'register_echo']
