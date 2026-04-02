"""Tests for the CLI beautification utilities."""

from io import StringIO
from textwrap import dedent

import pytest
from cyclopts.help import HelpEntry
from rich.console import Console
from rich.markdown import Markdown

from seedcase_soil.beautify_cli import (
    CONSOLE_THEME,
    _add_highlight_syntax,
    _format_param_help,
    pretty_print,
    print_if_verbose,
    run_without_tracebacks,
    setup_cli,
)

# Unit tests ====


def test_add_highlight_syntax_adds_bold_blue_to_flags():
    """Flags (starting with '-') should get bold blue markup."""
    result = _add_highlight_syntax("--source", str)
    assert result == "[bold blue]--source[/bold blue]"

    result = _add_highlight_syntax("-s", str)
    assert result == "[bold blue]-s[/bold blue]"


def test_add_highlight_syntax_adds_dim_to_positional_args():
    """Positional args should get dim markup."""
    result = _add_highlight_syntax("SOURCE", str)
    assert result == "[dim]<SOURCE>[/dim]"


def test_add_highlight_syntax_omits_placeholder_for_bool():
    """Boolean flags should not have a placeholder."""
    result = _add_highlight_syntax("verbose", bool)
    assert result == ""


def test_format_param_help_puts_flags_first():
    """Parameter help should show flags before positional args."""
    # HelpEntry uses positive_names/positive_shorts for flags
    # names is a computed property from positive_names
    entry = HelpEntry(
        positive_names=("--source", "-s"),
        type=str,
        description="The source file",
    )
    result = _format_param_help(entry)
    # Both flags get bold blue markup, sorted alphabetically
    assert "[bold blue]--source[/bold blue]" in result
    assert "[bold blue]-s[/bold blue]" in result
    # When sorted, '--' comes before '-' so --source is first
    assert result == "[bold blue]--source[/bold blue] [bold blue]-s[/bold blue]"


def test_pretty_print(capsys):
    """pretty_print should print the message."""

    pretty_print("test message")
    assert "test message" in capsys.readouterr().out


def test_print_if_verbose_when_verbose(capsys):
    """print_if_verbose should print when verbose is True."""

    print_if_verbose(True, "verbose message")
    assert "verbose message" in capsys.readouterr().out


def test_print_if_verbose_when_not_verbose(capsys):
    """print_if_verbose should not print when verbose is False."""

    print_if_verbose(False, "verbose message")
    assert capsys.readouterr().out == ""


def test_run_without_tracebacks_on_error(capsys):
    """run_without_tracebacks should print error panel and exit on exception."""

    def failing_app():
        raise ValueError("test error")

    with pytest.raises(SystemExit) as exc_info:
        run_without_tracebacks(failing_app)

    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    err = captured.err
    assert "ValueError" in err
    assert "test error" in err
    # Should not print a traceback
    assert "Traceback" not in captured.out
    assert "Traceback" not in captured.err


def test_styled_markdown_table_renders_box_and_header():
    """Markdown tables should render with a heavy-head box and column separators."""
    md = "| A | B |\n|---|---|\n| 1 | 2 |\n"
    out = StringIO()
    Console(file=out, theme=CONSOLE_THEME, no_color=True).print(Markdown(md))
    output = out.getvalue()
    assert "┏" in output  # heavy outer box top
    assert "┡" in output  # heavy-to-light header separator
    assert "┴" in output  # bottom border with column joins
    assert "A" in output
    assert "B" in output


# Integration tests ====


# Create a minimal test CLI to test the overall help formatting
app = setup_cli(
    name="test-cli",
    help="A test CLI for testing beautification.",
    config_name=".test.toml",
)


@app.command()
def build(
    source: str = "datapackage.json",
    verbose: bool = False,
    output_dir: str = "docs",
) -> None:
    """Build documentation from a file.

    Args:
        source: The source file to process.
        verbose: If True, print more details.
        output_dir: The output directory.
    """
    pass


_EXPECTED_HELP = dedent(
    """\
    Usage: test-cli COMMAND

    A test CLI for testing beautification.

    ╭─ Commands ─────────────────────────────────────────────────────────────────────────────╮
    │ <build>               Build documentation from a file.                                 │
    │ --help                Display this message and exit.                                   │
    │ --install-completion  Install shell completion for this application.                   │
    │ --version             Display application version.                                     │
    ╰────────────────────────────────────────────────────────────────────────────────────────╯
    """  # noqa
)

_EXPECTED_BUILD_HELP = dedent(
    """\
    Usage: test-cli build [ARGS]

    Build documentation from a file.

    ╭─ Parameters ───────────────────────────────────────────────────────────────────────────╮
    │ --source <SOURCE>          The source file to process.                                 │
    │                            [default: datapackage.json]                                 │
    │ --verbose                  If True, print more details.                                │
    │                            [default: False]                                            │
    │ --output-dir <OUTPUT-DIR>  The output directory.                                       │
    │                            [default: docs]                                             │
    ╰────────────────────────────────────────────────────────────────────────────────────────╯
    """  # noqa
)


@pytest.fixture
def console():
    return Console(
        width=90,
        force_terminal=True,
        highlight=False,
        color_system=None,
        legacy_windows=False,
    )


def test_main_help_page(capsys, console):
    """The main help page should have the correct format."""
    with pytest.raises(SystemExit):
        app(["--help"], console=console)
    assert capsys.readouterr().out == _EXPECTED_HELP


def test_command_help_page(capsys, console):
    """Command help should have the correct format."""
    with pytest.raises(SystemExit):
        app(["build", "--help"], console=console)
    assert capsys.readouterr().out == _EXPECTED_BUILD_HELP


# It was not possible to include these color markup tags directly in the help string
# test above because printing them out explicitly in the rich console messes up the
# column widths in cyclopts
def test_help_applies_rich_markup(capsys):
    """Help output should contain the markup tags (not rendered)."""
    markup_console = Console(
        width=90,
        force_terminal=False,
        highlight=False,
        color_system=None,
        markup=False,
        legacy_windows=False,
    )
    with pytest.raises(SystemExit):
        app(["build", "--help"], console=markup_console)
    output = capsys.readouterr().out
    assert "[bold blue]--source[/bold blue]" in output
    assert "[dim]<SOURCE>[/dim]" in output
    assert "[bold blue]--verbose[/bold blue]" in output
    # Boolean flags should not have a positional placeholder
    assert "[dim]<verbose>[/dim]" not in output
