from rich import box
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
