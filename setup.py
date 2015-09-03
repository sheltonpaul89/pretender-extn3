#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

from pretend_extended import __version__

setup(
    name='pretend-extended3',
    version='3.1',
    description='Fake servers for testing',
    long_description=open('README.rst').read(),
    author='Shelton Paul Infant',
    author_email='sheltonpaul89@gmail.com',
    url='https://github.com/sheltonpaul89/pretender-extn3',
    packages=find_packages(),
    install_requires=['bottle', 'argparse'],
    download_url='https://github.com/sheltonpaul89/pretender-extn3/tarball/3.1',
    #include_package_data=True,
    #package_data={
    #    '': ['*.txt', '*.rst'],
    #},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing',
    ],
)
