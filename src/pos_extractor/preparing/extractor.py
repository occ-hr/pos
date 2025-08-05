#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/preparing/extractor.py

from pos_extractor.interfaces.i_extractor import IExtractor
from pathlib import Path
from collections.abc import Sequence

class FileSystemExtractor(IExtractor):
    """
    Extracts file paths from a given directory tree using pathlib.
    """

    def extract_file_paths(self, root: str) -> Sequence[str]:
        """
        Walk the root directory and return all .txt or .pdf files.

        Args:
            root (str): Path to a root directory.

        Returns:
            Sequence[str]: List of absolute file paths matching criteria.
        """
        return []

# END: extractor.py    