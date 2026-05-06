from pathlib import Path

from seedir import seedir


def file_tree(path: Path) -> str:
    """Return the directory file tree with emojis as a string, excluding `.git` files.

    Args:
        path: The path to the directory.

    Returns:
        A string representation of the file tree with emojis.
    """
    # Check if the path is a directory and exists
    if not path.is_dir():
        raise ValueError(f"{path} is not a directory.")

    return seedir(  # type: ignore[no-any-return]
        path, style="emoji", exclude_folders=[".git"], first="folders", printout=False
    )
