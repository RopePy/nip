from nip.middleware.nipfile import (
    dependencies_selector, dev_dependencies_selector)


def write(lines, to):
    with open(to, 'w') as fs:
        fs.write("\n".join(lines))


def write_requirements_file(ctx, *args, **kwargs):
    dependencies = [*dependencies_selector(ctx).keys()]
    dev_dependencies = [*dev_dependencies_selector(ctx).keys()]

    if dependencies:
        write(dependencies, 'requirements.txt')

    if dev_dependencies:
        write(dev_dependencies, 'dev_dependencies.txt')
