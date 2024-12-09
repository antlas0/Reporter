#!/usr/bin/env python3

"""
copyright (c), 2021 antlas
"""


import os

from ..serialiser import Serialiser
from ..resources import ExportFormat

class CSVSerialiser(Serialiser):
    """[summary]

    output results as csv file
    Args:
        * Serialiser: [base class for serialisation]
    """
    def __init__(self) -> None:
        super().__init__()
        self._working_dir = None

    def set_working_dir(self, path:str) -> None:
        """
        Args:
            * path: [directory where all compilation process will be done]
        """
        if not os.path.isdir(path):
            raise RuntimeError

    def serialise(self, data: ExportFormat) -> None:
        """[summary]
        Args:
            * data: [the result in ExportFormat type]

        Returns:
            * [None]
        """
        return super().serialise()
