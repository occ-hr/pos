<<<<<<< HEAD
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/preparing/chunker.py

from pathlib import Path
from pos_extractor.interfaces.i_chunker import IChunker

class Chunker(IChunker):
    """
    Splits text files into chunks of fixed number of lines.
    """

    def chunk_files(self, 
                    _files: list[str], 
                    chunk_size: int = 100) -> list[str]:
        """
        Read files one at a time.
        Aggregate the lines from each file.
        Chunk the aggregate.

        Args:
            _files (list[Path | str]): List of file paths to read from.
            chunk_size (int): Number of lines per chunk.

        Returns:
            list[list[str]]: List of list of chunked read files.
        """
        if chunk_size <= 0:
            raise ValueError("Chunk_size must be > 0")
        
        _chunk: list[str] = []
        chunks: list[str] = []

        for _path in _files:
            with Path(_path).open(encoding='utf-8') as _f:
                for _line in _f:
                    _chunk.append(_line.rstrip("\n"))
                    if len(_chunk) == chunk_size:
                        chunks.append("\n".join(_chunk))
                        _chunk = []
        if _chunk:
            chunks.append("\n".join(_chunk))
        
        return chunks

# END: chunker.py
=======
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
>>>>>>> origin/main
