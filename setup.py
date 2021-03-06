#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='avcaesar_api',
    version='1.0.4',
    description='library and tool for AVCaesar API',
    author='Stéphane Emma',
    author_email='stephane@malware.lu',
    url='https://github.com/MalwareLu/avcaesar-api-python-driver',
    keywords=["avcaesar", "api"],
    packages=['avcaesar_api'],
    include_package_data=True,
    entry_points={'console_scripts': ['avcaesar.py = avcaesar_api.__main__:main']},
    install_requires=["requests>=1.0.0"],
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 3",
    ],
    license = "GPLv2",
)
