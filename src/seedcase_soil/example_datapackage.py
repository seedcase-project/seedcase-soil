"""Enum of built-in Data Package examples."""

from enum import StrEnum
from importlib.resources import files

from .parse_source import Address


class Example(StrEnum):
    """Available built-in example datapackage names."""

    simple = "simple"
    flora = "flora"
    flora_imperfect = "flora-imperfect"
    woolly = "woolly"

    @property
    def address(self) -> Address:
        """Return this example's local `Address`."""
        datapackage_path = files("seedcase_soil").joinpath(
            f"example-datapackages/{self.value}.json"
        )
        return Address(value=str(datapackage_path), local=True)
