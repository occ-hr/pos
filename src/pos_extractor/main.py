<<<<<<< HEAD
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/main.py

"""
Main entry point for the POS extractor application.
This module orchestrates the end-to-end process of part-of-speech (POS) extraction
from text files located in a specified input directory. It performs the following steps:
    1. Validates the input directory path.
    2. Extracts eligible file paths from the directory.
    3. Chunks file contents for batch processing.
    4. Loads categorization rules for POS tagging.
    5. Builds a custom NLP pipeline with rule injection.
    6. Runs POS extraction and displays sample results.
The pipeline is modular, leveraging components for validation, extraction, chunking,
rule loading, NLP pipeline construction, and POS tagging.
Intended for use as a standalone script or as part of a larger NLP processing workflow.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pos_extractor.preparing.validator import Validator
from pos_extractor.preparing.extractor import Extractor
from pos_extractor.preparing.chunker import Chunker
from pos_extractor.processing.loader import Loader
from pos_extractor.processing.builder import Builder
from pos_extractor.processing.runner import Runner

def main() -> None:
    # Hardcoded sample values — you can later replace with argparse or CLI flags
    _dir = "data/input/"
    rules = "data/rules/categories.json"
    _size = 10

    # Instantiate components
    _validator = Validator()
    _extractor = Extractor()
    _chunker = Chunker()
    _loader = Loader()
    _builder = Builder()
    _runner = Runner()

    # Step 1: Validate root path
    if not _validator.validate(_dir):
        print(f"Invalid input path: {_dir}")
        return

    print(f"[1] Validated path: {_dir}")

    # Step 2: Extract file paths
    _paths = _extractor.extract_paths(_dir)
    print(f"[2] Found {len(_paths)} eligible files.")

    if not _paths:
        print("No files to process.")
        return

    # Step 3: Chunk file contents
    chunks = _chunker.chunk_files(_paths, _size)
    print(f"[3] Chunked into {len(chunks)} chunks.")

    # Step 4: Load category rules
    rules = loader.load_categories(rules_file)
    print(f"[4] Loaded {len(rules)} categorization rules.")

    # Step 5: Build NLP pipeline
    nlp = builder.build_nlp_pipeline(rules)
    print("[5] NLP pipeline built with custom rule injector.")

    # Step 6: Run POS extraction
    tagged = runner.extract_pos(chunks, nlp)
    print(f"[6] POS tagging complete: {len(tagged)} tokens extracted.\n")

    # Display a sample
    for token, pos in tagged[:20]:
        print(f"{token:<15} {pos}")

    print("\n[Done]")


if __name__ == "__main__":
    main()
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/main.py

"""
Main entry point for the POS extractor application.
This module orchestrates the end-to-end process of part-of-speech (POS) extraction
from text files located in a specified input directory. It performs the following steps:
    1. Validates the input directory path.
    2. Extracts eligible file paths from the directory.
    3. Chunks file contents for batch processing.
    4. Loads categorization rules for POS tagging.
    5. Builds a custom NLP pipeline with rule injection.
    6. Runs POS extraction and displays sample results.
The pipeline is modular, leveraging components for validation, extraction, chunking,
rule loading, NLP pipeline construction, and POS tagging.
Intended for use as a standalone script or as part of a larger NLP processing workflow.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

def main() -> None:
    # Hardcoded sample values — later replace with argparse or CLI flags

    # Instantiate components

    # Step 1: Validate root path

    print("[1] Validated path: ")

    # Step 2: Extract file paths
    print("[2] Found eligible files.")

    if not True:  # Replace with actual condition to check for files
        print("No files to process.")

    # Step 3: Chunk file contents
    print("[3] Chunked into chunks.")

    # Step 4: Load category rules
    print("[4] Loaded categorization rules.")

    # Step 5: Build NLP pipeline
    print("[5] NLP pipeline built with custom rule injector.")

    # Step 6: Run POS extraction
    print("[6] POS tagging complete: tokens extracted.\n")

    # Display a sample

    print("\n[Done]")

if __name__ == "__main__":
    main()
>>>>>>> origin/main
