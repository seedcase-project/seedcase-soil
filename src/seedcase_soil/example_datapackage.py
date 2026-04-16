"""Helpers for creating example Data Package metadata."""

import json
from enum import StrEnum
from importlib.resources import files
from pathlib import Path
from typing import Any, cast


class ExampleDatapackageName(StrEnum):
    """Available built-in example datapackage names."""

    simple = "simple"
    flora = "flora"
    flora_imperfect = "flora-imperfect"


def load_example_datapackage(
    name: ExampleDatapackageName = ExampleDatapackageName.simple,
) -> dict[str, Any]:
    """Return an example datapackage dictionary."""
    datapackage_path = files("seedcase_soil").joinpath(
        f"example-datapackages/{name.value}.json"
    )
    return cast(dict[str, Any], json.loads(datapackage_path.read_text()))


def write_example_datapackage(
    directory: Path,
    name: ExampleDatapackageName = ExampleDatapackageName.simple,
) -> Path:
    """Write an example datapackage to a directory and return its path."""
    file_path = directory / "datapackage.json"
    file_path.write_text(json.dumps(load_example_datapackage(name=name)))
    return file_path
