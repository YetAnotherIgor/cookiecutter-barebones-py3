"""
A setuptools based setup module.
"""

import setuptools
import os
import sphinx.setup_command

# some common variables
PROJECT_AUTHOR = '{{ cookiecutter.author_name }}'
PROJECT_AUTHOR_EMAIL = '{{ cookiecutter.author_email }}'
PROJECT_COPYRIGHT = "2018, {}".format(PROJECT_AUTHOR)
PROJECT_VERSION = '{{ cookiecutter.version }}'


def read_long_description():
    """Read the long description text from the README.rst file"""
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.rst')
    with open(path, encoding='utf-8') as input_file:
        text = input_file.read()
    return text


setuptools.setup(
    author=PROJECT_AUTHOR,
    author_email=PROJECT_AUTHOR_EMAIL,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development ',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
    cmdclass={
        "sphinx_build": sphinx.setup_command.BuildDoc,
    },
    command_options={
        "sphinx_build": {
            'copyright': ('setup.py', PROJECT_COPYRIGHT),
            'nitpicky': ('setup.py', True),
            'project': ('setup.py', '{{ cookiecutter.project_pkg_name }}'),
            'release': ('setup.py', PROJECT_VERSION),
            'version': ('setup.py', PROJECT_VERSION),
            'warning_is_error': ('setup.py', True),
        },
    },
    data_files=[],
    description='{{ cookiecutter.project_description }}',
    entry_points={},
    extras_require={},
    include_package_data=True,
    install_requires=[
        "boltons >= 18.0.1, < 19.0.0",
    ],
    keywords='',
    license='BSD',
    long_description=read_long_description(),
    name='{{ cookiecutter.project_pkg_name }}',
    packages=[
        '{{ cookiecutter.project_module_name }}',
    ],
    package_data={},
    setup_requires=[
        'Sphinx >= 1.8.2',
        'pytest-runner >= 4.2',
    ],
    tests_require=[
        'mock >= 2.0.0',
        'pytest >= 4.0.0',
        'pytest-cov >= 2.6.0',
        'testfixtures >= 6.3.0',
    ],
    test_suite = 'tests',
    url='',
    version=PROJECT_VERSION,
)
