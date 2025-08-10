#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/interfaces/i_validator.py
# Provides interface contracts for input validation in the POS extractor module.

from typing import Protocol

class IValidator(Protocol):
    """
    Represents an adapter that enforces input validation.
    
    methods:
    - validate 
    """
    def validate(self, _inputs: str) -> bool:
        """
        Validates whether an input string is a proper target in its enviromnent.

        Args:
            user_input (str): input string from external source.

        Returns:
            bool: True if the input is valid, False otherwise.
        """
        ...  # Implementation must be provided by implementing classes

__all__ = ["IValidator"]

# END: i_validator.py
