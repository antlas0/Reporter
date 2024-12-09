#!/usr/bin/env python3

"""
copyright (c), 2021 antlas
"""


import argparse


class ArgumentParser:
    def __init__(self, title):
        self._arg_parser = argparse.ArgumentParser(description=title)
        self._args = None

    def run(self):
        """
        Parse the CLI arguments
        """
        assert(self._arg_parser is not None)
        self._arg_parser.add_argument(
            '-c', '--configuration-file',
            help='Specify a configuration file.',
            action="store",
            default="reporter.ini",
        )

        self._arg_parser.add_argument(
            '-i', '--input-directory',
            help='Specify a directory to import from.',
            action="store",
            default="input",
        )
        self._arg_parser.add_argument(
            '-o', '--output-directory',
            help='Specify a directory to store reports.',
            action="store",
            default="output",
        )
        self._args = vars(self._arg_parser.parse_args())

    def get_args(self):
        """
        Get the config
        """
        return self._args
