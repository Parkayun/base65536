from setuptools import setup
from setuptools.command.test import test


# Use pytest instead.
def run_tests(self):
    raise SystemExit(__import__('pytest').main(['-v']))
test.run_tests = run_tests


setup(
    name='base65536',
    version='0.1',
    packages=['base65536'],
    author='Ayun Park',
    author_email='iamparkayun@gmail.com',
    description='base65536',
    keywords='base65536',
    url='http://github.com/Parkayun/base65536',
    install_requires=['six'],
    tests_require=['pytest'],
)
