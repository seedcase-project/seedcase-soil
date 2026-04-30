"""Helpers for rendering command output in documentation."""

import os
import subprocess  # nosec B404
from collections.abc import Sequence
from io import StringIO

from rich.ansi import AnsiDecoder
from rich.console import Console


def format_output_for_docs(
    command: Sequence[str],
    *,
    width: int = 60,
) -> None:
    """Run a command and display compact, colored output in docs.

    This strips newlines, makes the output more narrow, enable overflow
    instead of wrapping, and remaps some colors. Currently everything
    except the output width is hard-coded to a certain style that emulates
    the look of the output when running in the terminal, but this could
    be parametrized later if the need arises.

    Args:
        command: The command to run, as a list of strings.
        width: The terminal width used when rendering command output.

    Examples:
        To run the command `cdp check --strict` and format the output:
        ```python
        format_output_for_docs(["cdp", "check", "--strict"])
        ```
    """
    from IPython.display import display

    full_env = os.environ.copy()
    full_env.update({"COLUMNS": str(width), "FORCE_COLOR": "1"})

    result = subprocess.run(  # nosec B603
        command,
        env=full_env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False,
    )
    display({"text/html": _html_output(result.stdout)}, raw=True)  # type: ignore[no-untyped-call]


def _html_output(output: str) -> str:
    pre_style = (
        "overflow-x: auto; line-height: normal; "
        "background-color: #1A1B26; color: #C0CAF5; "
        "border-radius: 0.5rem; padding: 0.5rem; "
        "font-family: Menlo, 'DejaVu Sans Mono', consolas, 'Courier New', monospace;"
    )
    code_style = (
        "white-space: pre; overflow-wrap: normal; word-break: normal; "
        "background: transparent; color: inherit;"
    )
    return (
        f'<pre style="{pre_style}">'
        f'<code style="{code_style}">{_ansi_to_html(output)}</code></pre>'
    )


def _ansi_to_html(output: str) -> str:
    console = Console(record=True, file=StringIO(), force_jupyter=False, width=200)
    lines = list(AnsiDecoder().decode(output.rstrip()))
    console.print(*lines, sep="\n", soft_wrap=True)
    html = console.export_html(inline_styles=True, code_format="{code}").rstrip()
    bold_style = "color: inherit; text-decoration-color: inherit; font-weight: bold"
    underline_style = "color: inherit; text-decoration-color: inherit"
    return (
        html.replace(
            '<span style="font-weight: bold">',
            f'<span style="{bold_style}">',
        )
        .replace(
            '<span style="text-decoration: underline">',
            '<span style="color: inherit; text-decoration-color: inherit; '
            'text-decoration: underline">',
        )
        .replace(
            "color: #008080; text-decoration-color: #008080; "
            "text-decoration: underline",
            f"{underline_style}; text-decoration: underline",
        )
        .replace("#003B4F", "inherit")
        .replace("#800000", "#F7768E")
        .replace("#000080", "#7AA2F7")
        .replace("#008000", "#9ECE6A")
        .replace("#008080", "#7DCFFF")
        .replace("#808080", "#8087A5")
        .replace("#808000", "#E0AF68")
    )
