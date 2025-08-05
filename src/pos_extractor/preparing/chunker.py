#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/preparing/chunker.py

from pathlib import Path
from pos_extractor.interfaces.i_chunker import IChunker

class LineChunker(IChunker):
    """
    Splits text files into chunks of fixed number of lines.
    """

    def chunk_files(self, 
                    file_paths: list[str], 
                    chunk_size: int = 100) -> list[str]:
        """
        Read files one at a time.
        Aggregate the lines from each file.
        Chunk the aggregate.

        Args:
            file_paths (list[Path | str]): List of file paths to read from.
            chunk_size (int): Number of lines per chunk.

        Returns:
            list[list[str]]: List of list of chunked read files.
        """
        chunks: list[str] = []

        return chunks

# END: chunker.py
