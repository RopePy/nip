#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.readlines()

with open('requirements_dev.txt') as test_requirements:
    test_requirements = test_requirements.readlines()


setup(
    name='nip.cli',
    version='0.3.1',
    author='Duroktar',
    description="nip isn't pip",
    long_description=readme + '\n\n' + history,
    author_email='duroktar@gmail.com',
    url='https://github.com/RopePy/nip',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    license="MIT License",
    zip_safe=False,
    keywords='nip',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'nip = nip.cli:main'
        ]
    },
    test_suite='tests',
    tests_require=test_requirements
)
