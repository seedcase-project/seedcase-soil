"""Tests for the CLI beautification utilities."""

from textwrap import dedent

import pytest
from cyclopts import App, Parameter
from cyclopts.help import HelpEntry
from rich.console import Console

from seedcase_soil.beautify_cli import (
    _add_highlight_syntax,
    _format_param_help,
    setup_cli,
)


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
    entry = HelpEntry(
        names=["SOURCE", "--source"],
        type=str,
        description="The source file",
    )
    result = _format_param_help(entry)
    # Flags should come first, then positional
    assert "[bold blue]--source[/bold blue]" in result
    assert "[dim]<SOURCE>[/dim]" in result
    # Check order: flag comes before placeholder
    assert result.index("[bold blue]") < result.index("[dim]")


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
