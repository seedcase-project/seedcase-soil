"""Helpers for creating example Data Package metadata."""

import json
from importlib.resources import files
from pathlib import Path
from typing import Any, cast


def load_example_datapackage(name: str = "simple") -> dict[str, Any]:
    """Return an example datapackage dictionary."""
    datapackage_path = files("seedcase_soil").joinpath(
        f"example-datapackages/{name}.json"
    )
    return cast(dict[str, Any], json.loads(datapackage_path.read_text()))


def write_example_datapackage(directory: Path, name: str = "simple") -> Path:
    """Write an example datapackage to a directory and return its path."""
    file_path = directory / "datapackage.json"
    file_path.write_text(json.dumps(load_example_datapackage(name=name)))
    return file_path
