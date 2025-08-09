<<<<<<< HEAD
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/interfaces/i_extractor.py

from collections.abc import Sequence
from typing import Protocol

class IExtractor(Protocol):
    """
    Represents an adapter that enforces extraction of directory into file paths.

    methods:
    - extract
    """

    def extract(self, _dirs: str) -> Sequence[str]:
        """
        Extracts file paths from input directory.

        Args:
            _dirs (str): The directory to scan.

        Returns:
            Sequence[str]: List of file paths as strings.
        """
        ...  # Implementation must be provided by implementing classes

__all__ = ["IExtractor"]

# END: i_extractor.py
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/schemas/interfaces/v1/i_extractor.py

from typing import Protocol
from collections.abc import Sequence

class IExtractor(Protocol):
    """
    Interface for extracting file paths from a directory or input source.
    
    Implementations should walk file trees and return lists of valid files
    (e.g., .txt, .pdf).
    """

    def extract_file_paths(self, root: str) -> Sequence[str]:
        """
        Recursively search a directory and return a list of file paths.

        Args:
            root (str): The root directory to scan.

        Returns:
            Sequence[str]: List of file paths as strings.
        """
        ...

# END: i_extractor.py
>>>>>>> origin/main
