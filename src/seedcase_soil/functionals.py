"""Small functional helpers shared across Seedcase packages."""

from itertools import chain, repeat
from typing import Callable, Iterable, TypeVar

In = TypeVar("In")
Out = TypeVar("Out")
Other = TypeVar("Other")
Result = TypeVar("Result")


def fmap(items: Iterable[In], fn: Callable[[In], Out]) -> list[Out]:
    """Apply `fn` to each element in `items`.

    The difference to the build-in `map()` is the order of the arguments
    and that the output is always a list.

    Args:
        items: The sequence of items, such as a list, array, or dict.
        fn: The function to apply.

    Returns:
        A list with the output values after the function is applied.

    """
    return list(map(fn, items))


def keep(items: Iterable[In], fn: Callable[[In], bool]) -> list[In]:
    """Keep elements in `items` where `fn` returns `True`.

    The difference to the built-in `filter()` is the order of the arguments,
    and that the output is always a list.

    Args:
        items: The sequence of items, such as a list, array, or dict.
        fn: The function with a condition that outputs a `bool`, which
            determines which items to keep.

    Returns:
        A list of the kept items.
    """
    return list(filter(fn, items))


def flat_fmap(items: Iterable[In], fn: Callable[[In], Iterable[Out]]) -> list[Out]:
    """Apply `fn` to each element in `items` and flatten one level.


    Args:
        items: The sequence of items, such as a list, array, or dict.
        fn: The function to apply to each element of `items`.

    Returns:
        A list that has one level removed.
    """
    return list(chain.from_iterable(map(fn, items)))


def pairwise_fmap(
    items1: list[In], items2: list[Other], fn: Callable[[In, Other], Result]
) -> list[Result]:
    """Apply `fn` to each pair of elements in `items1` and `items2`.

    If `items2` has only one element, that element is repeated
    to match the length of `items1`. Otherwise, both `item1` and
    `item2` must be the same length. The `fn` places `item1` in
    the first position and `item2` in the second position, e.g.
    `fn(item1, item2)`.

    Args:
        items1: The sequence of items, such as a list, array, or dict.
        items2: The sequence of items, such as a list, array, or dict.
        fn: The function to apply on each `items1` and `items2` (in pairwise combination).

    Returns:
        A list with the output values after applying the function.
    """
    if len(items2) == 1:
        items2 = list(repeat(items2[0], len(items1)))
    return list(map(fn, items1, items2))
