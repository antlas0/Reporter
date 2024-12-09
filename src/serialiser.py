#!/usr/bin/env python3

"""
copyright (c), 2021 antlas
"""

from abc import abstractmethod

class Serialiser:
    """[summary]
    This is an abstract class that serialises the export data
    ex: pdf, html, plotting
    """
    def __init__(self) -> None:
        pass

    @abstractmethod
    def serialise(self) -> None:
        """[summary]
        the method to override in each serialiser class
        """
        pass
