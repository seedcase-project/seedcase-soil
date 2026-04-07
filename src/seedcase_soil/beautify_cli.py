from itertools import repeat
from typing import Optional

from cyclopts import App, Parameter, config
from cyclopts.annotations import get_hint_name
from cyclopts.help import ColumnSpec, DefaultFormatter, DescriptionRenderer, HelpEntry
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
        "markdown.h1": "bold blue",
        "markdown.h2": "bold blue",
        "markdown.h3": "blue",
        "markdown.code": "yellow",
        "markdown.link": "underline cyan",
        "markdown.link_url": "underline cyan",
        "markdown.table.header": "blue",
        "markdown.table.border": "white",
    }
)


def setup_cli(name: str, help: str, config_name: str) -> App:
    """Setup the the Cyclopts app to use for the CLI.

    Args:
        name: The name of the package.
        help: The message that show with `--help`.
        config_name: The name of the configuration file.

    Returns:
        An Cyclopts app instance to be used as the CLI.
    """
    app = App(
        name=name,
        help=help,
        help_formatter=DefaultFormatter(
            column_specs=(
                ColumnSpec(renderer=_format_param_help),
                ColumnSpec(renderer=DescriptionRenderer(newline_metadata=True)),
            )
        ),
        default_parameter=Parameter(negative=(), show_default=True),
        console=Console(theme=CONSOLE_THEME),
        config=[
            config.Toml(
                config_name,
                search_parents=True,
                use_commands_as_keys=False,
            ),
            config.Toml(
                "pyproject.toml",
                root_keys=["tool", name],
                search_parents=True,
                use_commands_as_keys=False,
            ),
        ],
    )
    app.register_install_completion_command()
    return app


def _format_param_help(entry: HelpEntry) -> str:
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


def pretty_print(message: str) -> None:
    """Print with prettier formatting and highlighting.

    Args:
        message: Message to print.
    """
    rprint(message)


def print_if_verbose(verbose: bool, message: str) -> None:
    """Print with prettier formatting and highlighting.

    Args:
        verbose: Indication of whether verbose mode is enabled.
        message: Message to print.
    """
    if verbose:
        pretty_print(message)


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


def run_without_tracebacks(app: App, args: Optional[list[str]] = None) -> None:
    """Suppress traceback when running from CLI.

    Args:
        app: The Cyclopts app instance to run as the CLI.
        args: Any arguments to pass to the app upon launch. This is mostly for
            testing purposes so that we can emulate running `app --cmd`
            inside `run_without_tracebacks()`.

    """
    try:
        app(args)
    except Exception as e:
        _pretty_print_error(e)
        raise SystemExit(1)
