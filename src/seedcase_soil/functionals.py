"""Small functional helpers shared across Seedcase packages."""

from itertools import chain, repeat
from typing import Callable, Iterable, TypeVar

In = TypeVar("In")
Out = TypeVar("Out")
Other = TypeVar("Other")
Result = TypeVar("Result")


def fmap(x: Iterable[In], fn: Callable[[In], Out]) -> list[Out]:
    """Apply ``fn`` to each element in ``x`` and return a list."""
    return list(map(fn, x))


def keep(x: Iterable[In], fn: Callable[[In], bool]) -> list[In]:
    """Keep elements in ``x`` where ``fn`` returns ``True``."""
    return list(filter(fn, x))


def flat_fmap(items: Iterable[In], fn: Callable[[In], Iterable[Out]]) -> list[Out]:
    """Map each item with ``fn`` and flatten one level."""
    return list(chain.from_iterable(map(fn, items)))


def pairwise_fmap(
    x: list[In], y: list[Other], fn: Callable[[In, Other], Result]
) -> list[Result]:
    """Apply ``fn`` pairwise over two lists.

    If ``y`` has one element, that element is repeated to match the length of ``x``.
    """
    if len(y) == 1:
        y = list(repeat(y[0], len(x)))
    return list(map(fn, x, y))
