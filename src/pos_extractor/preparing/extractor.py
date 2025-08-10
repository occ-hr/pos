#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/preparing/extractor.py
# extracts file paths from directories.

from pos_extractor.interfaces.i_extractor import IExtractor
from pathlib import Path
from collections.abc import Sequence

class Extractor(IExtractor):
    """
    Concrete implementation of IExtractor for extracting file paths.
    
    Extracts file paths from direcory paths.
    """

    def extract(self, _dirs: list[str]) -> Sequence[str]:
        """
        Walk directory and return all .txt or .pdf files.

        Args:
            _dirs Sequence[str]: Paths to a directories.

        Returns:
            Sequence[str]: List of absolute file paths matching criteria.
        """
        paths = []
        for _dir_path in _dirs:
            
            return [str(_file_path) for _file_path in dir_Path(_path).rglob("*") if path.suffix in {".txt", ".pdf"}]
        
        return paths

# END: extractor.py
#     