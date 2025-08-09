<<<<<<< HEAD
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/processing/loader.py

import json
import csv
from collections.abc import Mapping
from pos_extractor.interfaces.i_loader import ILoader

class Loader(ILoader):
    """
    Loads categorization rules from a JSON or CSV file.
    """

    def load_categories(self, _path: str) -> Mapping[str, str]:
        """
        Parses a JSON or CSV file mapping phrases to categories.

        Args:
            file_path (str): Path to the categories file (.json or .csv).

        Returns:
            Mapping[str, str]: Dictionary mapping phrases to their category.
        """
        if _path.endswith(".json"):
            with open(_path, encoding="utf-8") as f:
                data = json.load(f)
                return {str(k): str(v) for k, v in data.items()}

        elif _path.endswith(".csv"):
            with open(_path, encoding="utf-8") as f:
                reader = csv.reader(f)
                return {str(row[0]): str(row[1]) for row in reader if len(row) >= 2}

        else:
            raise ValueError("Unsupported file format: must be .json or .csv")

# END: loader.py
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# src/pos_extractor/processing/loader.py

import json
import csv
from collections.abc import Mapping
from pos_extractor.interfaces.i_loader import ILoader

class RuleLoader(ILoader):
    """
    Loads categorization rules from a JSON or CSV file.
    """

    def load_categories(self, file_path: str) -> Mapping[str, str]:
        """
        Parses a JSON or CSV file mapping phrases to categories.

        Args:
            file_path (str): Path to the categories file (.json or .csv).

        Returns:
            Mapping[str, str]: Dictionary mapping phrases to their category.
        """
        
        return {"k1": "v1", "k2": "v2"}  # Placeholder implementation

# END: loader.py
>>>>>>> origin/main
