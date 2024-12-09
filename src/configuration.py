#!/usr/bin/env python3

"""
copyright (c), 2021 antlas
"""

import os
from configparser import ConfigParser

from .patterns import Singleton


class Configuration(metaclass=Singleton):
    def __init__(self):
        self._params = {}

    def get_config(self) -> dict:
        """
        Get configuration
        """
        return self._params

    def is_section_empty(self, name) -> bool:
        """
        Is the named section empty
        """
        if self._params[name] == {} or self._params[name] is None:
            return True
        else:
            return False

    def add_section(self, name) -> None:
        """
        Add a section in the configuration
        """
        if name not in self._params:
            self._params[name] = {}

    def set_param(self, section, name, value) -> None:
        """
        Set a param by name and value
        """
        if section not in self._params:
            self._params[section] = {}
        self._params[section][name] = value

    def get_sections(self) -> dict:
        """
        Get all sections
        """
        return self._params.keys()

    def get_section(self, section):
        """
        Get named section content
        """
        if section in self._params:
            return self._params[section]

    def has_section(self, section) -> bool:
        """
        Has configuration this section
        """
        if section in self._params:
            return True
        else:
            return False

    def get_param(self, section, name, defaultParam=None):
        """
        Get parameter value from name
        """
        if section not in self._params:
            return defaultParam
        else:
            if name not in self._params[section]:
                return defaultParam
            else:
                return self._params[section][name]

    def get_single_param(self, section, name, defaultParam=None) -> str:
        """
        Get a param by name
        """
        if section not in self._params:
            print(f"get single param for {section} {name} : no section")
            return defaultParam
        else:
            if name not in self._params[section]:
                print(f"get single param for {section} {name} : no name")
                return defaultParam
            else:
                if isinstance(self._params[section][name], list) and len(self._params[section][name]) >= 1:
                    return self._params[section][name][0]

    def does_section_hasKey(self, section, name) -> bool:
        """
        Has this section got this key
        """
        if section not in self._params:
            return False
        else:
            if name not in self._params[section]:
                return False
            else:
                return True

    def print_configuration(self) -> None:
        """
        Print the configuration to stdout
        """
        for section in self._params.keys():
            if self._params[section] is not None:
                print(f"[{section}]")
                for param in self._params[section]:
                    toPrint = str(param + " : " + str(self._params[section][param]))
                    print(toPrint)

    def read_configuration(self, path: str) -> None:
        """
        Read .ini configuration file
        """
        if not os.path.isfile(path):
            raise FileNotFoundError

        config = ConfigParser()
        config.read(path)
        for section in config.sections():
            if section not in self._params:
                self._params[section] = {}

            for param in config[section]:
                if param not in self._params[section]:
                    self._params[section][param] = None

                if str(config.get(section, param)) != str(self._params[section][param]):
                    self._params[section][param] = config.get(section, param)
