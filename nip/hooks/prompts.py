from nip.hooks.nipfile import update_nipfile


def get_package_name(ctx, get_input=input, **kwargs):
    package_name = get_input('Package Name: ')
    update_nipfile(ctx, {'name': package_name})


def get_author(ctx, get_input=input, **kwargs):
    authors_name = get_input('Author: ')
    update_nipfile(ctx, {'author': authors_name})


def get_license(ctx, get_input=input, **kwargs):
    software_license = get_input('License (MIT): ') or 'MIT'
    update_nipfile(ctx, {'license': software_license})
