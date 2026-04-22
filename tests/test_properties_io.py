"""Tests for the read_properties function."""

import json
from email.message import Message
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError

import pytest

from seedcase_soil.errors import (
    FileDoesNotExistError,
    HTTPDomainError,
    HTTPStatusError,
    JSONFormatError,
    NotJSONError,
)
from seedcase_soil.example_datapackage import Example
from seedcase_soil.parse_source import Address, parse_source
from seedcase_soil.properties_io import read_properties, write_properties

# read_properties: local file ====


def test_read_properties_local_filepath(datapackage_path, datapackage):
    """Reading a local datapackage.json file should return its contents."""
    address = Address(value=str(datapackage_path), local=True)
    result = read_properties(address)

    assert result == datapackage


def test_read_properties_local_dirpath(datapackage_path, datapackage):
    """Passing a path to a directory containing a datapackage.json should work."""
    address = parse_source(str(Path(datapackage_path).parent))
    result = read_properties(address)

    assert result == datapackage


def test_read_properties_raises_on_file_not_found():
    """A non-existent file should raise FileDoesNotExistError."""
    address = Address(value="file:///nonexistent/path/datapackage.json", local=True)

    with pytest.raises(FileDoesNotExistError):
        read_properties(address)


def test_read_properties_raises_on_malformed_json(tmp_path):
    """A file with malformed JSON should raise JSONFormatError."""
    json_file = tmp_path / "datapackage.json"
    json_file.write_text("{ invalid json }")

    address = Address(value=str(json_file), local=True)

    with pytest.raises(JSONFormatError):
        read_properties(address)


@pytest.mark.parametrize("example", list(Example))
def test_read_properties_reads_all_builtin_examples(example: Example) -> None:
    """Every built-in example should be readable with `read_properties`."""
    properties = read_properties(example.address)

    assert isinstance(properties, dict)
    assert len(properties) > 0


# read_properties: remote file ====


@pytest.mark.usefixtures("mocker")
def test_read_properties_remote_url(mocker, datapackage):
    """Reading a remote datapackage.json URL should return its contents."""
    mock_urlopen = mocker.patch("seedcase_soil.properties_io.request.urlopen")
    mock_response = mock_urlopen.return_value.__enter__.return_value
    mock_response.read.return_value = json.dumps(datapackage).encode()

    address = Address(value="https://example.com/datapackage.json", local=False)
    result = read_properties(address)

    assert result == datapackage
    mock_urlopen.assert_called_once_with("https://example.com/datapackage.json")


@pytest.mark.usefixtures("mocker")
def test_read_properties_raises_on_remote_invalid_json(mocker):
    """Remote URL returning malformed JSON should raise JSONFormatError."""
    mock_urlopen = mocker.patch("seedcase_soil.properties_io.request.urlopen")
    mock_response = mock_urlopen.return_value.__enter__.return_value
    mock_response.read.return_value = b"{ not json }"

    address = Address(value="https://example.com/datapackage.json", local=False)

    with pytest.raises(JSONFormatError):
        read_properties(address)


@pytest.mark.usefixtures("mocker")
def test_read_properties_raises_on_remote_404(mocker):
    """A remote URL returning 404 should raise HTTPStatusError."""
    mocker.patch(
        "seedcase_soil.properties_io.request.urlopen",
        side_effect=HTTPError(
            "https://example.com/datapackage.json", 404, "Not Found", Message(), None
        ),
    )

    address = Address(value="https://example.com/datapackage.json", local=False)

    with pytest.raises(HTTPStatusError):
        read_properties(address)


@pytest.mark.usefixtures("mocker")
def test_read_properties_raises_on_remote_dns_failure(mocker):
    """Remote URL with a non-existent domain should raise HTTPDomainError."""
    mocker.patch(
        "seedcase_soil.properties_io.request.urlopen",
        side_effect=URLError(reason=Exception("[Errno -2] Name or service not known")),
    )

    address = Address(
        value="https://nonexistent-domain-12345.com/datapackage.json", local=False
    )

    with pytest.raises(HTTPDomainError):
        read_properties(address)


@pytest.mark.usefixtures("mocker")
def test_read_properties_raises_on_non_json_content_type(mocker):
    """Remote URL returning non-JSON content type should raise NotJSONError."""
    mock_urlopen = mocker.patch("seedcase_soil.properties_io.request.urlopen")
    mock_response = mock_urlopen.return_value.__enter__.return_value
    mock_response.headers.get.return_value = "text/html; charset=utf-8"

    address = Address(value="https://example.com/datapackage.json", local=False)

    with pytest.raises(NotJSONError, match="Expected JSON but received 'text/html"):
        read_properties(address)


# write_properties:  ====


def test_write_properties_local_path(
    tmp_path: Path,
    datapackage: dict[str, Any],
) -> None:
    """Writing to a local file path should create datapackage.json."""
    output_path = tmp_path / "datapackage.json"
    write_properties(datapackage, output_path)

    assert output_path.exists()


def test_write_properties_accepts_string_path(
    tmp_path: Path,
    datapackage: dict[str, Any],
) -> None:
    """Writing to a string path should also work."""
    output_path = tmp_path / "datapackage.json"
    write_properties(datapackage, str(output_path))

    assert output_path.exists()


def test_write_properties_raises_on_missing_parent(
    tmp_path: Path,
    datapackage: dict[str, Any],
) -> None:
    """Writing to a path with missing parent directory should fail."""
    output_path = tmp_path / "missing" / "datapackage.json"

    with pytest.raises(FileNotFoundError):
        write_properties(datapackage, output_path)


def test_write_properties_raises_on_non_serializable(tmp_path: Path) -> None:
    """Writing non-JSON-serializable properties should fail."""
    output_path = tmp_path / "datapackage.json"

    with pytest.raises(TypeError):
        write_properties({"name": "test", "bad": Path("x")}, output_path)
