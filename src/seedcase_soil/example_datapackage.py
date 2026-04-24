"""Enum of built-in Data Package examples."""

from enum import StrEnum
from importlib.resources import files
from pathlib import Path

from .parse_source import Address


class Example(StrEnum):
    """Available built-in example datapackage names."""

    simple = "simple"
    flora = "flora"
    flora_imperfect = "flora-imperfect"
    woolly = "woolly"

    @property
    def path(self) -> Path:
        """Return this example's `Path`."""
        datapackage_path = files("seedcase_soil").joinpath(
            f"example-datapackages/{self.value}.json"
        )
        return Path(str(datapackage_path))

    @property
    def address(self) -> Address:
        """Return this example's `Address`."""
        return Address(value=str(self.path), local=True)
