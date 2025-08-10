#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/preparing/validator.py
# validates filepaths exist in exteernal enviroment.

"""
Concrete implementation of IValidator for validating filesystem paths.

Validates that the input string is a non-empty path that exists on the system.
"""

import os
from pos_extractor.interfaces.i_validator import IValidator

class Validator(IValidator):
    """
    Represents capability to validate inputs as paths.
    
    Validates that user input is a non-empty string containing at least one path-like component.
    """

    def validate(self, _inputs: str) -> bool:
        """
        Checks if the input string is a path.

        Args:
            _inputs (str): The input string input provided by the user.

        Returns:
            bool: True if input is a path, False otherwise.
        """
        return os.path.exists(_inputs)

# END: validator.py
