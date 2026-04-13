"""Functions for parsing the source for a Data Package."""

from dataclasses import dataclass
from pathlib import Path
from urllib import parse


@dataclass(frozen=True)
class Address:
    """A source parsed into an actual address."""

    value: str
    local: bool


def parse_source(source: str) -> Address:
    """Parse the source of a Data Package into a formal `Address`.

    Args:
        source: The string representation for the location of a Data Package's
            metadata, either as a path, `https`, or `gh`/`github` repository.

    Returns:
        A formal `Address` class.

    Raises:
        ValueError: If the `source` contains something other than what
            Seedcase can accept.

    Examples:
        ```{python}
        from seedcase_soil import parse_source

        parse_source("./datapackage.json")
        parse_source("gh:seedcase-project/example-seed-beetle@0.2.0")
        ```
    """
    split_source = parse.urlsplit(source)
    if split_source.scheme == "":
        split_source = split_source._replace(scheme="file")
    match split_source.scheme:
        case "file":
            return _convert_to_path(split_source)
        case "https":
            return _convert_to_https(split_source)
        case "gh" | "github":
            return _convert_to_github(split_source)
        case _:
            raise ValueError(
                "The source must be either a path to an existing file or "
                "folder or have one of the following prefixes: `https:`, "
                "`gh:`, `github:`"
            )


def _convert_to_path(source: parse.SplitResult) -> Address:
    path = Path(source.path).resolve()
    if path.is_dir():
        path /= "datapackage.json"
    source = source._replace(path=path.as_posix())
    return Address(value=source.geturl(), local=True)


def _convert_to_https(source: parse.SplitResult) -> Address:
    return Address(value=source.geturl(), local=False)


def _convert_to_github(source: parse.SplitResult) -> Address:
    full_path = f"{source.netloc}{source.path}"
    if "@" in full_path:
        owner_repo, ref = full_path.rsplit("@", 1)
    else:
        owner_repo, ref = full_path, "main"

    _check_github_source(owner_repo, ref, full_path)

    return Address(
        value=source._replace(
            scheme="https",
            netloc="raw.githubusercontent.com",
            path=f"/{owner_repo}/{ref}/datapackage.json",
        ).geturl(),
        local=False,
    )


def _check_github_source(owner_repo: str, ref: str, original: str) -> None:
    parts = owner_repo.split("/")
    if len(parts) != 2 or not all(parts):
        raise ValueError(
            f"Invalid GitHub source '{original}': must be in format "
            "'gh:owner/repo', 'github:owner/repo', or with an optional "
            "'@ref' (e.g., 'gh:owner/repo@v1.0.0')."
        )

    if not ref:
        raise ValueError(
            f"Invalid GitHub source '{original}': ref after '@' cannot be empty."
        )
