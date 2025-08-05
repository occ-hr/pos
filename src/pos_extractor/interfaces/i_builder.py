#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/schemas/interfaces/v1/i_builder.py
from typing import Mapping, Protocol

class IBuilder(Protocol):
    """
    Interface for constructing a SpaCy NLP pipeline with custom components.
    """

    def build_nlp_pipeline(self, rules: Mapping[str, str]) -> Language:
        """
        Build and return an NLP pipeline, optionally injecting rule-based logic.

        Args:
            rules (Mapping[str, str]): A dictionary mapping phrases to categories.

        Returns:
            Language: A fully configured SpaCy pipeline.
        """
        ...
        
# END: i_builder.py
