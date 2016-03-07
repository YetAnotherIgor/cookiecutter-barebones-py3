# -*- coding: utf-8 -*-

"""
A setuptools based setup module.

Loosely based on https://github.com/pypa/sampleproject/blob/master/setup.py

"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # Basic project identifiers
    name='{{ cookiecutter.project_pkg_name }}',
    version='{{ cookiecutter.version }}',

    # Description and home url
    description='{{ cookiecutter.project_description }}',
    long_description=long_description,
    url='',

    # Author contact info
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',

    # License
    license='BSD',

    # Classifiers and keywords
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='cookiecutter',

    # Packages and tests
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    test_suite = 'tests',

    # Runtime dependencies to be installed via setuptools
    install_requires=[],

    # Setup.py dependencies
    setup_requires=[
        'pytest-runner>=2.7', 
        'pytest>=2.8.0',
	'pytest-cov',
    ],

    # Test-time dependencies
    tests_require=[
        'mock>=1.3.0',
    ],

    # "Extras" dependencies
    extras_require={},

    # Data files
    package_data={},
    data_files=[],

    # Executable entry points
    entry_points={},
)
