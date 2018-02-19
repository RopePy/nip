SETUP_PY_TEMPLATE = """# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

def readlines(fo):
    try: rv = fo.readlines()
    except FileNotFoundError: rv = []
    finally: return rv

with open('requirements.txt') as requirements_file:
    requirements = readlines(requirements_file)

with open('requirements_dev.txt') as test_requirements_file:
    test_requirements = readlines(test_requirements_file)


setup(
    name='%(name)s',
    version=%(version)s,
    packages=find_packages(),
    install_requires=requirements,
    tests_require=test_requirements
)
"""
