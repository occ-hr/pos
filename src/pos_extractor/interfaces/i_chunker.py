<<<<<<< HEAD
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/interfaces/i_chunker.py

from collections.abc import Sequence
from typing import Protocol

class IChunker(Protocol):
    """
    Represents an adapter.
    Such that enfocing of chunking into chunks is done.
    
    methods.
    - chunk
    """

    def chunk(self, _files: Sequence[list[str]], _size: int) -> Sequence[list[str]]:
        """
        Chunks file contents into lines of the given size.

        Args:
            _files (Sequence[list[str]]): List of file paths to read from.
            _size (int): Number of lines per chunk.

        Returns:
            Sequence[list[str]]: List of text chunks.
        """
        ...  # Implementation must be provided by implementing classes.

__all__ = ["IChunker"]

# END: i_chunker.py
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/schemas/interfaces/v1/i_chunker.py

from typing import Protocol

class IChunker(Protocol):
    """
    Interface for splitting files into text chunks.
    
    Implementations may chunk by lines, characters, or other delimiters.
    """

    def chunk_files(self, file_paths: list[list[str]], chunk_size: int) -> list[list[str]]:
        """
        Break file contents into chunks of a given size.

        Args:
            file_paths (Sequence[str]): List of file paths to read from.
            chunk_size (int): Number of lines per chunk.

        Returns:
            Sequence[str]: List of text chunks.
        """
        ...

# END: i_chunker.py
>>>>>>> origin/main
