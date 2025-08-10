from dataclasses import dataclass, field
from typing import Any, Tuple, Optional, Dict
from uuid import UUID, uuid4

from .base import TimestampedEntity

@dataclass
class Token(TimestampedEntity):
    """Entity: Represents a generic token or item with optional span and attributes."""
    id: UUID = field(default_factory=uuid4)
    value: Any = None
    span: Optional[Tuple[int, int]] = None
    attributes: Dict[str, Any] = field(default_factory=dict)  # pyright: ignore[reportUnknownVariableType]
