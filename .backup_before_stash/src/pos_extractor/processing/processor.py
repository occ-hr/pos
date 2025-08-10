from typing import Dict, Any

class Processor:
    def run(self, params: Dict[str, Any]) -> None:
        # Example: pretend to load and build tokens
        print("[processing] loading data and building tokens/categories")
        params["processed_count"] = params.get("processed_count", 0) + 1
