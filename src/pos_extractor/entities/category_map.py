from typing import Dict, Optional, Any

class CategoryMap:
    """Entity: In-memory mapping container for category lookups."""
    def __init__(self, initial: Optional[Dict[Any, Any]] = None):
        self._map: Dict[Any, Any] = initial.copy() if initial else {}

    def get(self, key: Any) -> Optional[Any]:
        return self._map.get(key)

    def add(self, key: Any, value: Any) -> None:
        self._map[key] = value

    def all(self) -> Dict[Any, Any]:
        return self._map.copy()

    def __contains__(self, key: Any) -> bool:
        return key in self._map
