#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/processing/builder.py

from spacy.language import Language
from spacy.tokens import Doc
from spacy.lang.en import English
from typing import Callable
from collections.abc import Mapping
from pos_extractor.interfaces.i_builder import IBuilder

# pyright: reportUnknownMemberType=false
# pyright: reportUntypedFunctionDecorator=false

@Language.factory("custom_rule_injector")
def build_components(_nlp: Language, _name: str, _rules: Mapping[str, str]) -> Callable[[Doc], Doc]:
    """
    Factory function that builds a custom rule-based pipeline component.

    Args:
        nlp (Language): The NLP pipeline.
        name (str): The component name in the pipeline.
        rules (Mapping[str, str]): A dictionary of phrase-category rules.

    Returns:
        Callable[[Doc], Doc]: The pipeline component.
    """

    def get_docs(_docs: Doc) -> Doc:
        # Placeholder: use rules to annotate or tag the doc
        # Example: print matched rule phrases (you will customize this)
        matches = [phrase for phrase in _rules if phrase in get_docs.text]
        if matches:
            print(f"[MATCHES]: {matches}")
        return _docs

    return component


class CustomNLPBuilder(IBuilder):
    """
    Builds an NLP pipeline with an injected rule-based component.
    """

    def build_pipeline(self, rules: Mapping[str, str]) -> Language:
        """
        Create and configure a SpaCy pipeline with injected rules.

        Args:
            rules (Mapping[str, str]): A map of phrase → category.

        Returns:
            Language: The customized SpaCy pipeline.
        """
        _nlp = English()

        # Add the factory component and inject rules via config
        _nlp.add_pipe("custom_rule_injector", config={"rules": rules}, last=True)

        return _nlp


# END: buildere.py
