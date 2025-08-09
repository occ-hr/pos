from typing import Dict, Any

class Trainer:
    def run(self, params: Dict[str, Any]) -> None:
        # Example: pretend to train/update a model using injected categories
        print("[training] training model with current parameters")
        params["trained"] = True
