"""Shared fixtures for tests."""

import json

import pytest

from seedcase_soil import Example, read_properties


@pytest.fixture
def datapackage():
    """Return a data package dict with resources."""
    return read_properties(Example.simple.address)


@pytest.fixture
def datapackage_path(tmp_path, datapackage):
    """Create a temporary datapackage.json file and return its path as a string."""
    file_path = tmp_path / "datapackage.json"
    file_path.write_text(json.dumps(datapackage))
    return str(file_path)
