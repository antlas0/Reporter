#!/usr/bin/env python3

"""
copyright (c), 2021 antlas
"""

import os
import glob
from typing import Optional, List

from .resources import ImportFormat


class Importer:
    """
    Class devoted to import data of interest
    from sources

    All returned data is in the ImportFormat
    """
    def __init__(self, config: dict):
        self._config = config

    def import_from_dir(self, path: str, file_format: str="csv") -> Optional[ImportFormat]:
        """[summary]

        Args:
            * path: [directory data input]

        Returns:
            * [Imported data]
        """
        if not os.path.isdir(path):
            raise RuntimeError

        cb_table = {
            "csv": self.import_from_csv_files,
        }

        fois = glob.glob(path + f"*.{format}")

        data = None
        if fois:
            data = cb_table[format](fois)

        return data


    def import_from_csv_files(self, files: List[str]) -> ImportFormat:
        """[summary]
        Given a list of CSV files, return one object
        in ImportFormat

        Args:
            * files: [list of csv files path]

        Returns:
            * [Imported data]
        """
        pass

    def import_from_database(self, uri:str) -> Optional[ImportFormat]:
        """
        Import remote data to ImportFormat
        """
        pass

    def run(self) -> Optional[ImportFormat]:
        """
        Import data regarding the configuration
        """
        # forcing reading from disk as of now
        self.import_from_dir(self._config["input"]["directory"])
