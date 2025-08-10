# src/pos_extractor/use_cases/pos_extract.py
from typing import List

class POSExtractUseCase:
    """Orchestrates the complete POS-extraction workflow."""

    def __init__(
        self,
        validator, extractor, chunker,
        loader, builder, runner
    ) -> None:
        self._validator = validator
        self._extractor = extractor
        self._chunker = chunker
        self._loader = loader
        self._builder = builder
        self._runner = runner

    def execute(self, user_inputs: List[str]) -> List[dict]:
        """High-level happy path."""
        valid_paths = self._validator.validate(user_inputs)         # 1
        file_paths = self._extractor.extract(valid_paths)           # 2
        chunks     = self._chunker.chunk(file_paths)                # 3
        inj_map    = self._loader.load()                            # 4
        nlp        = self._builder.build(inj_map)                   # 5
        results    = self._runner.run(chunks, nlp)                  # 6
        return results