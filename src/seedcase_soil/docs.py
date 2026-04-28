"""Helpers for rendering command output in documentation."""

import os
import subprocess
from collections.abc import Sequence
from io import StringIO

from rich.ansi import AnsiDecoder
from rich.console import Console


def format_output_for_docs(
    command: Sequence[str],
    *,
    width: int = 62,
) -> None:
    """Run a command and display compact, colored output in docs.

    Args:
        command: The command to run, as a list of strings.
        width: The terminal width used when rendering command output.

    """
    from IPython.display import display

    full_env = os.environ.copy()
    full_env.update({"COLUMNS": str(width), "FORCE_COLOR": "1"})

    result = subprocess.run(
        command,
        env=full_env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False,
    )
    display({"text/html": _html_output(result.stdout)}, raw=True)


def _html_output(output: str) -> str:
    pre_style = (
        "overflow-x: auto; line-height: normal; "
        "font-family: Menlo, 'DejaVu Sans Mono', consolas, 'Courier New', monospace;"
    )
    code_style = "white-space: pre; overflow-wrap: normal; word-break: normal;"
    return (
        f'<pre style="{pre_style}">'
        f'<code style="{code_style}">{_ansi_to_html(output)}</code></pre>'
    )


def _ansi_to_html(output: str) -> str:
    console = Console(record=True, file=StringIO(), force_jupyter=False, width=200)
    lines = list(AnsiDecoder().decode(output.rstrip()))
    console.print(*lines, sep="\n", soft_wrap=True)
    html = console.export_html(inline_styles=True, code_format="{code}").rstrip()
    return (
        html.replace("#800000", "#E75C58")
        .replace("#000080", "#7AA2F7")
        .replace("#008000", "#00A250")
        .replace("#008080", "#60C6C8")
        .replace("#808080", "#8087A5")
    )
