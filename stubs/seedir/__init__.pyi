# Type stub for seedir.
# mypy reads .pyi files from the `stubs/` directory (configured via `mypy_path` in
# `pyproject.toml`).
from pathlib import Path
from typing import Any

# "= ..." at an argument means that the actual value shouldn't matter to mypy.
# ": ..." as the function body means no implementation (fine in .pyi stubs).
def seedir(
    path: str | Path,
    style: str = ...,
    exclude_folders: list[str] | None = ...,
    first: str = ...,
    printout: bool = ...,
    **kwargs: Any,
) -> str | None: ...
