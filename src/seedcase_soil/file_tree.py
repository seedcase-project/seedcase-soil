from pathlib import Path

import seedir as sd


def file_tree(path: Path) -> str:
    """Show file tree excluding `.git` files.

    Args:
        path: The path to the package directory.

    Returns:
        A string representation of the file tree.
    """
    # Check if the path is a directory and exists
    if not path.is_dir():
        raise ValueError(f"{path} is not a directory.")

    return sd.seedir(
        path,
        style="emoji",
        exclude_folders=[".git"],
        first="folders",
        printout=False,
    )
