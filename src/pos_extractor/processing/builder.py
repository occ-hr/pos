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
def build_custom_rule_component(nlp: Language, name: str, rules: Mapping[str, str]) -> Callable[[Doc], Doc]:
    """
    Factory function that builds a custom rule-based pipeline component.

    Args:
        nlp (Language): The NLP pipeline.
        name (str): The component name in the pipeline.
        rules (Mapping[str, str]): A dictionary of phrase-category rules.

    Returns:
        Callable[[Doc], Doc]: The pipeline component.
    """

    def component(doc: Doc) -> Doc:
        # Placeholder: use rules to annotate or tag the doc
        # Example: print matched rule phrases (you will customize this)

        return doc

    return component


class CustomNLPBuilder(IBuilder):
    """
    Builds an NLP pipeline with an injected rule-based component.
    """

    def build_nlp_pipeline(self, rules: Mapping[str, str]) -> Language:
        """
        Create and configure a SpaCy pipeline with injected rules.

        Args:
            rules (Mapping[str, str]): A map of phrase → category.

        Returns:
            Language: The customized SpaCy pipeline.
        """
        nlp = English()

        # Add the factory component and inject rules via config

        return nlp


# END: buildere.py
