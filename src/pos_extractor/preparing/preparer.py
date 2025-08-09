from typing import Dict, Any

class Preparer:
    def run(self, params: Dict[str, Any]) -> None:
        # Example: normalize input directories and seed defaults
        print("[preparing] validating inputs and seeding defaults")
        params.setdefault("input_paths", [])
        params.setdefault("batch_size", 128)
