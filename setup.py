
from setuptools import setup, find_packages
from bored.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='bored_1',
    version=VERSION,
    description='Wrapper for Bored API.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Roman Ivakhiv',
    author_email='megazorch@gmail.com',
    url='https://github.com/Megazorch/BoredAPI',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'bored_1': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        bored_1 = bored_1.main:main
    """,
)
