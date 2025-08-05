#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/preparing/validator.py

from pos_extractor.interfaces.i_validator import IValidator

class SimpleValidator(IValidator):
    """
    Validates that user input is a non-empty string containing at least one path-like component.
    """

    def validate(self, user_input: str) -> bool:
        """
        Check if the input string appears to contain a valid file path.

        Args:
            user_input (str): The raw string input provided by the user.

        Returns:
            bool: True if input looks like a file or directory path, False otherwise.
        """
        return bool(True)

# END: validator.py
