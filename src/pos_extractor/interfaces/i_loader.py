<<<<<<< HEAD
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/interfaces/i_loader.py

from typing import Protocol
from collections.abc import Mapping

class ILoader(Protocol):
    """
    Represents an adapter.
    Such that enforcing of loading is done.

    methods:
    - load
    """

    def load(self, _path: str) -> Mapping[str, str]:
        """
        Loads file.

        Args:
            _path (str): File path.

        Returns:
            Mapping[str, str]: Mapping (with phrase-category pairs).
        """
        ...  # Implementation must be provided by implementing classes.

__all__ = ["ILoader"]

# END: i_loader.py
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/schemas/interfaces/v1/i_loader.py

from typing import Protocol
from collections.abc import Mapping

class ILoader(Protocol):
    """
    Interface for loading a category ruleset from a file.

    Files may be in JSON or CSV format and map phrases to categories.
    """

    def load_categories(self, file_path: str) -> Mapping[str, str]:
        """
        Load phrase-to-category mapping from a file.

        Args:
            file_path (str): File path to a JSON or CSV ruleset.

        Returns:
            Mapping[str, str]: Dictionary with phrase-category pairs.
        """
        ...

# END: i_loader.py
>>>>>>> origin/main
