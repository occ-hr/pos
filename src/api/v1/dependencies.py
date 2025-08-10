# src/api/v1/dependencies.py
# shared FastAPI dependencies for v1 routes (e.g., orchestrator factory, DB session).

"""
an injectable dependency; easy to swap/mock later.
"""

from functools import lru_cache
from pos_extractor.container import Orchestrator
from pos_extractor.entities.job_spec import Component
from pos_extractor.preparing.preparer import Preparer
from pos_extractor.processing.processor import Processor
from pos_extractor.training.trainer import Trainer

@lru_cache
def get_orchestrator() -> Orchestrator:
    return Orchestrator(components={
        Component.PREPARING: Preparer(),
        Component.PROCESSING: Processor(),
        Component.TRAINING: Trainer(),
    })