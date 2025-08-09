from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from uuid import UUID, uuid4

from .base import TimestampedEntity

@dataclass
class Document(TimestampedEntity):
    """Entity: Generic container for document-like data."""
    id: UUID = field(default_factory=uuid4)
    content: Optional[Any] = None
    children: List[Any] = field(default_factory=list)  # pyright: ignore[reportUnknownVariableType]
    metadata: Dict[str, Any] = field(default_factory=dict)  # pyright: ignore[reportUnknownVariableType]
