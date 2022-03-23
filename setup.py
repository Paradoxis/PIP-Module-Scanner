#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import re
import io
import os
import sys
from shutil import rmtree

from setuptools import setup, Command

NAME = 'pip-module-scanner'

DESCRIPTION = (
    'Scans your Python project for all installed third party pip '
    'libraries and generates a requirements.txt based output.')

URL = 'https://github.com/Paradoxis/PIP-Module-Scanner'
EMAIL = 'luke@paradoxis.nl'
AUTHOR = 'Luke Paris (Paradoxis)'
REQUIRES_PYTHON = '>=2.7.0'

REQUIRED = []
EXTRA = {
    'test': [
        'codecov',
        'coverage',
        'requests==2.19.1',
        'flask==1.0.2'
    ],
    'dev': [
        'twine'
    ]
}


# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = ('\n' + f.read()).strip()

with io.open(os.path.join(here, 'pip_module_scanner', '__init__.py'), encoding='utf-8') as init:
    VERSION = re.search(r'__version__ = [\'"]([\d.]+)[\'"]', init.read()).group(1)

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()


# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=['flask_unsign'],
    entry_points={
        'console_scripts': ['pip-module-scanner=pip_module_scanner.__main__:main'],
    },
    install_requires=REQUIRED,
    extras_require=EXTRA,
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    cmdclass={
        'upload': UploadCommand,
    },
)