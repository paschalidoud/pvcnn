#!/usr/bin/env python

"""Setup pvcnn."""

from itertools import dropwhile
from setuptools import find_packages, setup
from os import path

import numpy as np

from Cython.Build import cythonize
from distutils.extension import Extension


def collect_docstring(lines):
    """Return document docstring if it exists"""
    lines = dropwhile(lambda x: not x.startswith('"""'), lines)
    doc = ""
    for line in lines:
        doc += line
        if doc.endswith('"""\n'):
            break

    return doc[3:-4].replace("\r", "").replace("\n", " ")


def collect_metadata():
    meta = {}
    with open(path.join("pvcnn", "__init__.py")) as f:
        lines = iter(f)
        meta["description"] = collect_docstring(lines)
        for line in lines:
            if line.startswith("__"):
                key, value = map(lambda x: x.strip(), line.split("="))
                meta[key[2:-2]] = value[1:-1]

    return meta


def get_extensions():
    return []

def get_install_requirements():
    return [
        "numpy",
        "cython",
        "torch",
        "torchvision",
    ]

def setup_package():
    with open("README.md") as f:
        long_description = f.read()
    meta = collect_metadata()
    print(meta)
    setup(
        name="pvcnn",
        version=meta["version"],
        description=meta["description"],
        long_description=long_description,
        maintainer=meta["maintainer"],
        maintainer_email=meta["email"],
        url=meta["url"],
        license=meta["license"],
        classifiers=[
            "Intended Audience :: Science/Research",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Topic :: Scientific/Engineering",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
        ],
        packages=find_packages(exclude=["docs", "tests", "scripts"]),
        install_requires=get_install_requirements(),
        ext_modules=get_extensions()
    )


if __name__ == "__main__":
    setup_package()

