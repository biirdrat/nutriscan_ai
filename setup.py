"""
Setup script for the Nutriscan AI package.

This script uses setuptools to package the Nutriscan AI application. It reads the version
from the __init__.py file, and specifies package metadata and dependencies.

Functions:
    read_version(): Reads and returns the version from the src/GUI/__init__.py file.
"""

from setuptools import setup, find_packages

def read_version():
    """
    Reads the version from the src/GUI/__init__.py file.

    This function opens the specified __init__.py file, looks for a line starting with
    __version__, and extracts the version number from that line.

    Returns:
        str: The version number as a string.

    Raises:
        RuntimeError: If the __version__ string cannot be found.
    """
    with open("src/GUI/__init__.py", encoding='utf-8') as f:
        for line in f:
            if line.startswith('__version__'):
                return line.strip().split('=')[1].strip().strip('"').strip("'")
    return ""
setup(
    name='nutriscan_ai',
    author='Steven Tu',
    author_email='22tsteven@gmail.com',
    version=read_version(),
    packages=find_packages(),
    install_requires=[
    ],
)
