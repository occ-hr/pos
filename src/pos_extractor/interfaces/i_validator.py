#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/schemas/interfaces/v1/i_validator.py
from typing import Protocol

class IValidator(Protocol):
    """
    Defines the interface for validating user input strings.

    A conforming implementation must determine whether
    the input string appears to represent a valid file or directory path.
    """
    def validate(self, user_input: str) -> bool:
        """
        Evaluate whether the input string is a valid target (e.g., a path).

        Args:
            user_input (str): Raw input string from user or external source.

        Returns:
            bool: True if the input is considered valid, False otherwise.
        """
        ...  # Implementation should be provided by concrete classes

# END: i_validator.py