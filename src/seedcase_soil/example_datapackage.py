"""Helpers for creating example Data Package metadata."""

import json
from pathlib import Path
from typing import Any


def example_datapackage() -> dict[str, Any]:
    """Return an example datapackage dictionary."""
    return {
        "name": "test-package",
        "title": "Test Package",
        "description": "A test datapackage",
        "version": "1.0.0",
        "licenses": [{"name": "MIT"}],
        "resources": [
            {
                "name": "data",
                "path": "data.csv",
                "schema": {
                    "fields": [
                        {"name": "id", "type": "integer"},
                        {"name": "name", "type": "string"},
                    ]
                },
            },
            {
                "name": "data2",
                "path": "data2.csv",
                "schema": {
                    "fields": [
                        {"name": "id", "type": "integer"},
                        {"name": "age", "type": "integer"},
                    ]
                },
            },
        ],
    }


def write_example_datapackage(directory: Path) -> Path:
    """Write the example `datapackage.json` to a directory and return its path."""
    file_path = directory / "datapackage.json"
    file_path.write_text(json.dumps(example_datapackage()))
    return file_path
