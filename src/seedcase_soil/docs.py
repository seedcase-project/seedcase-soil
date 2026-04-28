"""Helpers for rendering command output in documentation."""

import os
import subprocess
from collections.abc import Mapping, Sequence
from io import StringIO
from pathlib import Path

from rich.ansi import AnsiDecoder
from rich.console import Console


def format_output_for_docs(
    command: Sequence[str],
    *,
    width: int = 72,
    cwd: str | Path | None = None,
    env: Mapping[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    """Run a command and display compact, colored output in docs.

    Args:
        command: The command to run, as a list of strings.
        width: The terminal width used when rendering command output.
        cwd: The working directory to run the command from.
        env: Environment variables to add or override.

    Returns:
        The completed process from running the command.
    """
    from IPython.display import display

    full_env = os.environ.copy()
    full_env.update({"COLUMNS": str(width), "FORCE_COLOR": "1"})
    if env is not None:
        full_env.update(env)

    result = subprocess.run(
        command,
        cwd=cwd,
        env=full_env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False,
    )
    display({"text/html": _html_output(result.stdout)}, raw=True)
    return result


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
        .replace("#008000", "#00A250")
        .replace("#008080", "#60C6C8")
    )
