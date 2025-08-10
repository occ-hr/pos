#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/interfaces/i_loader.py
# Provides interface contracts for loaders in the POS extractor module.

from typing import Protocol
from collections.abc import Mapping

class ILoader(Protocol):
    """
    Represents an adapter.
    Such that enforcing of loading is done.

    methods:
    - load
    """

    def load(self, _path: str) -> Mapping[str, str]:
        """
        Loads file.

        Args:
            _path (str): File path.

        Returns:
            Mapping[str, str]: Mapping (with phrase-category pairs).
        """
        ...  # Implementation must be provided by implementing classes.

__all__ = ["ILoader"]

# END: i_loader.py
