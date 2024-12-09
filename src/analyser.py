#!/usr/bin/env python3

"""
copyright (c), 2021 antlas
"""


from .resources import ImportFormat, ExportFormat


class Analyser:
    """
    Given data as ImportFormat, performs
    data analysis to provide plots, metrics, and such
    gathered in ExportFormat

    This is the domain-driven part
    """
    def __init__(self, config: dict, data: ImportFormat):
        self._config = config
        self._imported_data = data

    def plot_timeline(self):
        """
        Generate a timeline plot of the ImportFormat data
        """
        pass

    def run(self) -> ExportFormat:
        """
        Call all analysis methods on the ImportFormat data
        to generate the ExportFormat data containing metrics
        """
        pass
