#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/interfaces/i_extractor.py

from collections.abc import Sequence
from typing import Protocol

class IExtractor(Protocol):
    """
    Represents an adapter that enforces extraction of directory into file paths.

    methods:
    - extract
    """

    def extract(self, _dirs: str) -> Sequence[str]:
        """
        Extracts file paths from input directory.

        Args:
            _dirs (str): The directory to scan.

        Returns:
            Sequence[str]: List of file paths as strings.
        """
        ...  # Implementation must be provided by implementing classes

__all__ = ["IExtractor"]

# END: i_extractor.py
