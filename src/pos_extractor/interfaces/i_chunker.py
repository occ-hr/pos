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
