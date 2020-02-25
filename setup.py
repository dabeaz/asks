#!/usr/bin/env python3

from setuptools import setup
from sys import version_info

setup(
    name='asks',
    description='asks - async http',
    long_description='asks is an async http lib for curio',
    license='MIT',
    version='2.3.7',
    author='Mark Jameson - aka theelous3',
    url='https://github.com/theelous3/asks',
    packages=['asks'],
    install_requires=['h11', 'curio']
    tests_require=['pytest', 'curio', 'overly'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
