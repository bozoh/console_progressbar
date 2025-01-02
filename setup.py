"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""


from setuptools import setup, find_packages
from codecs import open
from os import path
from importlib import import_module

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='console_progressbar',
    version=import_module('console_progressbar').__version__,
    description='A simple progress bar for console',
    long_description=long_description,
    url='https://github.com/bozoh/console_progressbar',
    author='Carlos Alexandre S. da Fonseca',
    author_email='carlos.alexandre@outlook.com',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    license = 'MIT',
    keywords='progressbar console',
    python_requires='>=2.7',
    setup_requires=['pytest-runner'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['pytest', 'coverage', 'mock'],
        'testing': ['pytest', 'coverage', 'mock'],
    },
)
