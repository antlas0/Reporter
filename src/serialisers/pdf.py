#!/usr/bin/env python3

"""
copyright (c), 2021 antlas
"""

import os
import copy
import logging
import subprocess
from dataclasses import fields
from tempfile import mkdtemp
from shutil import copyfile, copytree

from src.serialiser import Serialiser
from ..resources import PDFDetails
from .template.template_pdf import template_content

class PDFSerialiser(Serialiser):
    """
    Serialize data as pdf
    """
    def __init__(self):
        super().__init__()
        self._working_dir = None

    def set_working_dir(self, path:str) -> None:
        """
        Args:
            * path: [directory where all compilation process will be done]
        """
        if not os.path.isdir(path):
            raise RuntimeError

        self._working_dir = path

    def serialise(self, path:str, details:PDFDetails) -> bool:
        """[summary]
        Args:
            * path: [the path to the generated file]
            * details: [details on the content of the file]

        Returns:
            * [boolean telling the success status]
        """
        to_print = self._override_template(details)
        return self._compile_pdf(path, to_print)

    def _override_template(self, details:PDFDetails) -> str:
        """[summary]
        Args:
            * details: [details on the content of the file]

        Returns:
            * [the pdf content to be generated]
        """
        template = copy.deepcopy(template_content)

        for field in fields(details):
            value = getattr(details, field.name)
            if getattr(details, field.name) is not None:
                template = template.replace(field.name, getattr(details, field.name))

        return template

    def _compile_pdf(self, path:str, to_print:str) -> bool:
        """[summary]
        Args:
            * path: [the file to generate]
            * to_print: [the file content]

        Returns:
            * [boolean success or fail]
        """
        temp_dir = mkdtemp()
        tex_path = os.path.join(temp_dir, "report.tex")
        with open(tex_path, "w") as f:
            f.write(to_print)

        if not os.path.isfile(tex_path):
            raise RuntimeError

        copyfile(
            os.path.join("src", "serialisers", "template", "template.cls"),
            dst=os.path.join(temp_dir, "template.cls")
        )

        copytree(
            os.path.join("src", "serialisers", "template", "fonts"),
            dst=os.path.join(temp_dir, "fonts"),
            dirs_exist_ok=True,
        )

        command = f"/usr/bin/xelatex -synctex=1 -interaction=nonstopmode report.tex {path}".split(" ")
        process = subprocess.run(list(command), cwd=temp_dir)

        if process.returncode != 0:
            logging.warn(f"PDF compilation failed in {temp_dir}, with process output {process}")
            return False

        copyfile(
            os.path.join(temp_dir, "report.pdf"),
            dst=os.path.join(self._working_dir, "report.pdf")
        )
        return True
