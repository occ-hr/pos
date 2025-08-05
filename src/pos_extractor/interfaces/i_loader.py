#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/schemas/interfaces/v1/i_loader.py

from typing import Protocol
from collections.abc import Mapping

class ILoader(Protocol):
    """
    Interface for loading a category ruleset from a file.

    Files may be in JSON or CSV format and map phrases to categories.
    """

    def load_categories(self, file_path: str) -> Mapping[str, str]:
        """
        Load phrase-to-category mapping from a file.

        Args:
            file_path (str): File path to a JSON or CSV ruleset.

        Returns:
            Mapping[str, str]: Dictionary with phrase-category pairs.
        """
        ...

# END: i_loader.py
