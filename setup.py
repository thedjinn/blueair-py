#!/usr/bin/env python3

"""Package setup script."""

import codecs
import os
import re

from setuptools import find_packages, setup  # type: ignore
from typing import List

def get_absolute_path(*args: str) -> str:
    """Transform relative pathnames into absolute pathnames."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), *args)

def get_contents(*args: str) -> str:
    """Get the contents of a file relative to the source distribution directory."""
    return codecs.open(get_absolute_path(*args), "r", "UTF-8").read()

def get_version(*args: str) -> str:
    """Extract the version number from a Python module."""
    contents = get_contents(*args)
    metadata = dict(re.findall('__([a-z]+)__\\s+=\\s+[\'"]([^\'"]+)', contents))
    return metadata["version"]

def get_requirements(*args: str) -> List[str]:
    """Get requirements from pip requirement files."""
    requirements = set()

    with open(get_absolute_path(*args)) as handle:
        for line in handle:
            # Strip comments.
            line = re.sub(r"^#.*|\s#.*", "", line)

            # Ignore empty lines
            if line and not line.isspace():
                requirements.add(re.sub(r"\s+", "", line))

    return sorted(requirements)

setup(
    name="blueair",
    version=get_version("blueair", "__init__.py"),
    description="Unofficial Python client for BlueAir air purifiers",
    long_description=get_contents("README.rst"),
    url="https://blueair.readthedocs.io",
    author="Emil Loer",
    author_email="emil@codelle.com",
    license="MIT",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "blueair = blueair.cli:run",
        ]
    },
    package_data={
        "blueair": ["py.typed"]
    },
    install_requires=get_requirements("requirements.txt"),
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Communications",
        "Topic :: Internet",
        "Topic :: Office/Business",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: System :: Hardware",
        "Topic :: System :: Logging",
        "Topic :: Utilities",
        "Typing :: Typed"
    ]
)
