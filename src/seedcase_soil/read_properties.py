"""Function for reading Data Package properties."""

import json
from pathlib import Path
from typing import Any
from urllib import parse, request
from urllib.error import HTTPError, URLError

from .errors import (
    FileDoesNotExistError,
    HTTPDomainError,
    HTTPStatusError,
    JSONFormatError,
    NotJSONError,
)
from .parse_source import Address

JSON_CONTENT_TYPES = ("application/json", "application/ld+json", "application/geo+json")
Properties = dict[str, Any]


def read_properties(address: Address) -> Properties:
    """Read properties from a local or remote datapackage.

    Args:
        address: The formal representation for the location of a Data Package's
            metadata.

    Returns:
        A dictionary with datapackage metadata.

    Raises:
        FileDoesNotExistError:
            If the file cannot be found.
        JSONFormatError:
            If the JSON files is malformatted.
        HTTPStatusError:
            If an HTTP error is encountered.
        HTTPDomainError:
            If the domain cannot be found.

    Examples:
        ```{python}
        from seedcase_soil import parse_source, read_properties

        address = parse_source("gh:seedcase-project/example-seed-beetle@0.2.0")
        read_properties(address)
        ```
    """
    datapackage: Properties
    if address.local:
        path = Path(parse.urlsplit(address.value).path)
        try:
            with open(path) as properties_file:
                datapackage = json.load(properties_file)
        except FileNotFoundError:
            raise FileDoesNotExistError(str(path))
        except json.JSONDecodeError as e:
            raise JSONFormatError(str(path), str(e))
    else:
        try:
            with request.urlopen(address.value) as open_url:  # nosec B310
                content_type = open_url.headers.get("Content-Type", "")
                if not content_type.startswith(JSON_CONTENT_TYPES + ("text/plain",)):
                    main_type = content_type.split(";")[0].strip()
                    raise NotJSONError(address.value, main_type)
                datapackage = json.load(open_url)
        except HTTPError as e:
            raise HTTPStatusError(address.value, e.code, e.reason)
        except URLError as e:
            if "Name or service not known" in str(
                e.reason
            ) or "getaddrinfo failed" in str(e.reason):
                raise HTTPDomainError(address.value)
            raise JSONFormatError(address.value, str(e))
        except json.JSONDecodeError as e:
            raise JSONFormatError(address.value, str(e))
    return datapackage
