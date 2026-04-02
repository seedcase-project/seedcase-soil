from itertools import repeat
from typing import Optional

from cyclopts.annotations import get_hint_name
from cyclopts.help import HelpEntry
from rich import box
from rich import print as rprint
from rich.console import Console
from rich.highlighter import ReprHighlighter
from rich.panel import Panel
from rich.text import Text
from rich.theme import Theme

# To style markdown tables with a box (pipes) surrounding each column
# instead of only a horizontal line after the table header
box.SIMPLE = box.HEAVY_HEAD

CONSOLE_THEME = Theme(
    {
        "markdown.h1": "bold yellow",
        "markdown.h2": "bold yellow",
        "markdown.h3": "italic yellow",
        "markdown.code": "blue",
        "markdown.link": "underline cyan",
        "markdown.link_url": "underline cyan",
        "markdown.table.header": "yellow",
        "markdown.table.border": "white",
    }
)

HELP_CONSOLE_THEME = Theme(
    {
        "markdown.code": "yellow not reverse",
    }
)


def format_param_help(entry: HelpEntry) -> str:
    """Re-structure the parameter help into a more readable format."""
    # Sort to put the flag first (eg `--source SOURCE` instead of the default
    # `SOURCE --source`)
    names = map(_add_highlight_syntax, sorted(entry.names), repeat(entry.type))
    return f"{' '.join(names)}".strip()


def _add_highlight_syntax(name: str, entry_type: Optional[type]) -> str:
    """Add markup character to highlight in colors, etc where desired."""
    formatted_name = f"[bold blue]{name}[/bold blue]"
    if not name.startswith("-"):
        # Matching the `dim` used by default in cyclopts for `choices` and
        # `defaults` in the description
        formatted_name = f"[dim]<{name}>[/dim]"

        # Don't output redundant value placeholder for boolean flags
        if get_hint_name(entry_type) == "bool":
            formatted_name = ""
    return formatted_name


def pretty_print(verbose: bool, message: str) -> None:
    """Print with prettier formatting and highlighting."""
    if verbose:
        rprint(message)


def _pretty_print_error(e: Exception) -> None:
    console = Console(stderr=True)
    text = Text.from_markup(str(e))
    # Make `text` appear as if it was printed by rich.print
    pretty_text = ReprHighlighter()(text)
    console.print(
        Panel(
            pretty_text,
            title=type(e).__name__,
            border_style="red",
            box=box.ROUNDED,
            title_align="left",
        )
    )


def run_without_tracebacks(app) -> None:
    """Suppress traceback when running from CLI."""
    try:
        app()
    except Exception as e:
        _pretty_print_error(e)
        raise SystemExit(1)
