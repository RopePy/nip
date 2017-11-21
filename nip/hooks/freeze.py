# from nip.middleware.echo import echo_selector
# from nip.providers.pip import silent_pip_freeze


def nip_freeze(ctx, *args, **kwargs):
    """
        TODO: Doesn't play well with how we install packages
        from the nip file. Either update nip install to read
        the requirements file, or parse frozen requirements
        in an after hook and add them to the nipfile. I think
        option number 1 is the best solution. But number 2
        may be more versatile, especially if we're already
        trying to keep track of deps and their versions.
    """
    # echo = echo_selector(ctx)
    # echo('Freezing packages..')
    # silent_pip_freeze()
