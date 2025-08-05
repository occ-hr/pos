#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/interfaces/i_runner.py

from typing import Protocol
from collections.abc import Sequence
from spacy.language import Language

class IRunner(Protocol):
    """
    Interface for running NLP inference on input chunks.
    """

    def extract_pos(self, text_chunks: Sequence[str], nlp: Language) -> list[tuple[str, str]]:
        """
        Run NLP pipeline and extract POS-tagged tokens from text.

        Args:
            text_chunks (Sequence[str]): List of input texts to analyze.
            nlp (Language): The SpaCy pipeline to use.

        Returns:
            list[tuple[str, str]]: List of (token, POS) tuples.
        """
        ...

# END: i_runner.py
