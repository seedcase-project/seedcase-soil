"""Small functional helpers shared across Seedcase packages."""

from itertools import chain, repeat
from typing import Callable, Iterable, TypeVar

In = TypeVar("In")
Out = TypeVar("Out")
Other = TypeVar("Other")
Result = TypeVar("Result")


def fmap(items: Iterable[In], fn: Callable[[In], Out]) -> list[Out]:
    """Apply `fn` to each element in `items`.

    The difference from the build-in map is the order of the arguments
    and that the output is always a list.

    Args:
        items: The sequence of items.
        fn: The function to apply.

    Returns:
        A list with the output values after function application.

    """
    return list(map(fn, items))


def keep(items: Iterable[In], fn: Callable[[In], bool]) -> list[In]:
    """Keep elements in `items` where `fn` returns `True`.

    The difference from the built-in filter is the order of the arguments,
    and that the output is always a list.

    Args:
        items: The sequence of items.
        fn: The function that decides which items to keep.

    Returns:
        A list of the items to keep.
    """
    return list(filter(fn, items))


def flat_fmap(items: Iterable[In], fn: Callable[[In], Iterable[Out]]) -> list[Out]:
    """Apply `fn` to each element in `items` and flatten one level.

    The difference from the built-in filter is the order of the arguments,
    and that the output is always a list.

    Args:
        items: The sequence of items.
        fn: The function that decides which items to keep.

    Returns:
        A list of the items to keep.
    """
    return list(chain.from_iterable(map(fn, items)))


def pairwise_fmap(
    items1: list[In], items2: list[Other], fn: Callable[[In, Other], Result]
) -> list[Result]:
    """Apply `fn` to each pair of elements in `items1` and `items2`.

    If `items1` has only one element, that element is repeated
    to match the length of `items2`.

    Args:
        items1: The first sequence of items.
        items2: The second sequence of items.
        fn: The function to apply

    Returns:
        A list with the output values after function application.
    """
    if len(items2) == 1:
        items2 = list(repeat(items2[0], len(items1)))
    return list(map(fn, items1, items2))
