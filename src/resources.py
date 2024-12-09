#!/usr/bin/env python3

"""
copyright (c), 2021 antlas
"""


from dataclasses import dataclass
from typing import Optional, Dict, Any
from enum import Enum
import pandas as pd

from .serialiser import Serialiser

class Milestone(Enum):
    unknown=0
    first=1


@dataclass(frozen=True)
class CommercialData:
    customer_id: str
    country: str
    milestone:Milestone


@dataclass(frozen=True)
class ImportFormat:
    data: pd.DataFrame


@dataclass(frozen=True)
class ExportFormat:
    data: Dict[str, Any]
    serialiser: Optional[Serialiser] = None


import os

@dataclass()
class PDFDetails:
    """
    Stores pdf details to generate the file
    """
    author1: Optional[str] = None
    email1: Optional[str] = None
    title1: Optional[str] = None
    image1: Optional[str] = None

    def __post_init__(self) -> None:

        # be sure to deal with an absolute path
        if self.image1 is not None:
                self.image1 = os.path.abspath(self.image1)
