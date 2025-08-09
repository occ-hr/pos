<<<<<<< HEAD
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/interfaces/i_builder.py

from typing import Protocol
from collections.abc import Mapping
from spacy.language import Language

class IBuilder(Protocol):
    """
    Represents an adapter.
    Such that enforcing of building of Language is done.
    """

    def build(self, _rules: Mapping[str, str]) -> Language:
        """
        Builds NLP pipeline by injecting rule-based logic.

        Args:
            _rules (Mapping[str, str]): A dictionary mapping phrases to categories.

        Returns:
            Language: A fully configured SpaCy pipeline.
        """
        ...  # Implementation must be provided by concrete classes

__all__ = ["IBuilder"]

# END: i_builder.py
=======
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
>>>>>>> origin/main
