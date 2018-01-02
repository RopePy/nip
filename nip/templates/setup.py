SETUP_PY_TEMPLATE = """# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.readlines()

with open('requirements_dev.txt') as test_requirements:
    test_requirements = test_requirements.readlines()

setup(
    name='%(name)s',
    version=%(version)s,
    packages=find_packages(),
    install_requires=requirements,
    tests_require=test_requirements
)
"""
