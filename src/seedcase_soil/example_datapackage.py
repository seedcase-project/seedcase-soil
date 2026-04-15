"""Helpers for creating example Data Package metadata."""

import json
from importlib.resources import files
from pathlib import Path
from typing import Any

EXAMPLE_DATAPACKAGE_PATH = files("seedcase_soil").joinpath("datapackages/simple.json")


def example_datapackage() -> dict[str, Any]:
    """Return an example datapackage dictionary."""
    return json.loads(EXAMPLE_DATAPACKAGE_PATH.read_text())


def write_example_datapackage(directory: Path) -> Path:
    """Write the example `datapackage.json` to a directory and return its path."""
    file_path = directory / "datapackage.json"
    file_path.write_text(json.dumps(example_datapackage()))
    return file_path
