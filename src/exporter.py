#!/usr/bin/env python3

"""
copyright (c), 2021 antlas
"""


from typing import Dict

from .resources import ExportFormat
from .serialisers.pdf import PDFSerialiser, PDFDetails


class Exporter:
    """
    Class devoted to import data of interest
    from sources

    All returned data is in the ExportFormat
    """
    def __init__(self, config: dict, data: ExportFormat):
        self._export_data = data
        self._config = config
        self._working_directory = self._config["output"]["directory"]
        self._serialiser = self._config["output"]["serialiser"]

    def generate_plots_to_disk(self, data: ExportFormat) -> Dict[str, str]:
        """[summary]
        Args:
            * data: [data to generate the plots from]

        Returns:
            * [a dict with the data id and its plot path on disk]
        """
        pass

    def generate_pdf(self, resources: Dict[str, str]) -> bool:
        """[summary]
        Args:
            * resources: [the dict that tells where to find images or content on disk]

        Returns:
            * [success or fail]
        """
        details = PDFDetails(
            author1=self._config["pdf"]["author1"],
            title1=self._config["pdf"]["title1"],
            image1=None,
        )

        pdf = PDFSerialiser()
        pdf.set_working_dir(self._config["output"]["directory"])
        return pdf.serialise("report.pdf", details)

    def export_to_database(self) -> bool:
        """
        Export data to database
        """
        pass

    def run(self) -> bool:
        """
        Export data to a specified destination
        """
        if self._serialiser == "pdf":
            resources = self.generate_plots_to_disk(self._export_data)
            self.generate_pdf(resources)
