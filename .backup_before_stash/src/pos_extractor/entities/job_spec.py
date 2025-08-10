from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any, Dict, List
from uuid import UUID, uuid4

class Component(Enum):
    PREPARING = auto()
    PROCESSING = auto()
    TRAINING = auto()

@dataclass
class JobSpec:
    """Entity: Defines a pipeline run configuration."""
    id: UUID = field(default_factory=uuid4)
    name: str = ""
    steps: List[Component] = field(default_factory=lambda: [
        Component.PREPARING,
        Component.PROCESSING,
        Component.TRAINING
    ])
    params: Dict[str, Any] = field(default_factory=dict)  # pyright: ignore[reportUnknownVariableType]
