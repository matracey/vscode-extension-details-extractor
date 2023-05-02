"""
vscode-extension-details-extractor
=================================

A Python script that extracts the short description of one or more Visual Studio Code extensions.

This script uses the Visual Studio Marketplace API to retrieve the details of one or more extensions and extract their short descriptions. The short descriptions are then printed to the console.

Usage:
    vscode-extension-details-extractor <extension_id>...
"""
from setuptools import setup

setup(
    name='vscode-extension-details-extractor',
    version='0.1',
    description='A Python script that extracts the short description of one or more Visual Studio Code extensions.',
    author='Martin Tracey',
    author_email='opentoscope@outlook.com',
    py_modules=['vscode_extension_details_extractor'],
    install_requires=[
        'beautifulsoup4',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'vscode-extension-details-extractor=vscode_extension_details_extractor:main',
        ],
    },
)
