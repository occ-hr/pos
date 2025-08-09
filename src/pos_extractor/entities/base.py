from dataclasses import dataclass, field
from datetime import datetime, timezone
from abc import ABC

@dataclass
class TimestampedEntity(ABC):
    """Abstract base for entities that track creation and update timestamps."""
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def touch(self) -> None:
        """Update the `updated_at` timestamp to current UTC time."""
        self.updated_at = datetime.now(timezone.utc)
