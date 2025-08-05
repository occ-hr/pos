#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/processing/runner.py

from pos_extractor.interfaces.i_runner import IRunner
from spacy.language import Language
from collections.abc import Sequence

class POSRunner(IRunner):
    """
    Runs a SpaCy NLP pipeline on input text and extracts (token, POS) pairs.
    """

    def extract_pos(self, 
                    text_chunks: Sequence[str], 
                    nlp: Language) -> list[tuple[str, str]]:
        """
        Process chunks through the NLP pipeline and extract part-of-speech tags.

        Args:
            text_chunks (Sequence[str]): List of text chunks to process.
            nlp (Language): The customized SpaCy pipeline.

        Returns:
            list[tuple[str, str]]: A list of (token.text, token.pos_) tuples.
        """

        return [("a1", "a2")] # Placeholder for actual implementation
# END: runner.py
