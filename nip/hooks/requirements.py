from nip.config.paths import DEV_REQUIREMENTS_FILE, REQUIREMENTS_FILE
from nip.middleware.nipfile import (
    dependencies_selector, dev_dependencies_selector)
from nip.utils.path import file_write_lines

def write_requirements_file(ctx, *args, **kwargs):
    dependencies = [*dependencies_selector(ctx).keys()]
    dev_dependencies = [*dev_dependencies_selector(ctx).keys()]

    if dependencies:
        file_write_lines(dependencies, REQUIREMENTS_FILE)

    if dev_dependencies:
        file_write_lines(dev_dependencies, DEV_REQUIREMENTS_FILE)
