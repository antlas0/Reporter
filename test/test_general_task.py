#!/usr/bin/env python3


"""
copyright (c), 2021 antlas
"""


import os
import subprocess


def test_generate_dependencies():
    """[summary]
    Use this test to update the requirements
    """
    requirements_file = "requirements.txt"
    command = ["pigar"]

    if not os.path.isfile(requirements_file):
        raise FileNotFoundError

    original_deps = None
    with open(requirements_file, "r") as f:
        original_deps = f.read()

    process = subprocess.run(command)
    new_deps = None
    with open(requirements_file, "r") as f:
        new_deps = f.read()

    assert(process.returncode == 0 and original_deps == new_deps)


def test_generate_documentation():
    """[summary]
    TODO: use the CI for that
    """
    doi = "src"
    command = ["pdoc", "-o", "doc", doi]

    if not os.path.isdir(doi):
        raise RuntimeError

    process = subprocess.run(command)

    assert(process.returncode == 0)
