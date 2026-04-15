"""Helpers for creating example Data Package metadata."""

import json
from importlib.resources import files
from pathlib import Path
from typing import Any


def load_datapackage(name: str = "simple") -> dict[str, Any]:
    """Return an example datapackage dictionary."""
    datapackage_path = files("seedcase_soil").joinpath(f"datapackages/{name}.json")
    return json.loads(datapackage_path.read_text())


def write_datapackage(directory: Path, name: str = "simple") -> Path:
    """Write the example `datapackage.json` to a directory and return its path."""
    file_path = directory / "datapackage.json"
    file_path.write_text(json.dumps(load_datapackage(name=name)))
    return file_path
