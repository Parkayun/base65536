import os

from setuptools import setup
from setuptools.command.test import test


# Include __about__.py.
__dir__ = os.path.dirname(__file__)
about = {}
with open(os.path.join(__dir__, 'base65536', '__about__.py')) as f:
    exec(f.read(), about)


# Use pytest instead.
def run_tests(self):
    raise SystemExit(__import__('pytest').main(['-v']))
test.run_tests = run_tests


setup(
    name='base65536',
    version=about['__version__'],
    packages=['base65536'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    description=about['__description__'],
    keywords=about['__keywords__'],
    url=about['__url__'],
    install_requires=['six'],
    tests_require=['pytest'],
)
