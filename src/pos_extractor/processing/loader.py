#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/processing/loader.py

import json
import csv
from collections.abc import Mapping
from pos_extractor.interfaces.i_loader import ILoader

class RuleLoader(ILoader):
    """
    Loads categorization rules from a JSON or CSV file.
    """

    def load_categories(self, file_path: str) -> Mapping[str, str]:
        """
        Parses a JSON or CSV file mapping phrases to categories.

        Args:
            file_path (str): Path to the categories file (.json or .csv).

        Returns:
            Mapping[str, str]: Dictionary mapping phrases to their category.
        """
        
        return {"k1": "v1", "k2": "v2"}  # Placeholder implementation

# END: loader.py
