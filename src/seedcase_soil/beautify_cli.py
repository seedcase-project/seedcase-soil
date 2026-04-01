from rich import box
from rich.console import Console
from rich.highlighter import ReprHighlighter
from rich.panel import Panel
from rich.text import Text


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


def main(app) -> None:
    """Suppress traceback when running from CLI."""
    try:
        app()
    except Exception as e:
        _pretty_print_error(e)
        raise SystemExit(1)
