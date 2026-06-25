"""Numeric and collection helpers — pure, deterministic utilities.

Standard library only. Each function is a self-contained transform with
clear input/output behavior, ideal for behavior verification.
"""
from collections import Counter
from typing import Any, Hashable, List, Sequence, TypeVar

T = TypeVar("T")
H = TypeVar("H", bound=Hashable)


def chunk_list(items: Sequence[T], size: int) -> List[List[T]]:
    """Split a list into consecutive chunks of at most ``size`` items.

    >>> chunk_list([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    """
    if size <= 0:
        raise ValueError("size must be positive")
    return [list(items[i:i + size]) for i in range(0, len(items), size)]


def deduplicate_preserving_order(items: Sequence[H]) -> List[H]:
    """Remove duplicates from a list while keeping first-seen order.

    >>> deduplicate_preserving_order([3, 1, 3, 2, 1])
    [3, 1, 2]
    """
    seen: set[H] = set()
    result: List[H] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def most_common_element(items: Sequence[H]) -> H:
    """Return the most frequently occurring element in a non-empty list.

    On a tie, returns the element that appears first among the tied ones
    (per collections.Counter ordering).

    >>> most_common_element([1, 2, 2, 3, 3, 3])
    3
    """
    if not items:
        raise ValueError("items must not be empty")
    return Counter(items).most_common(1)[0][0]


def percentage(part: float, whole: float, ndigits: int = 2) -> float:
    """Return ``part`` as a percentage of ``whole``, rounded to ndigits.

    Returns 0.0 when whole is 0 (avoids division by zero).

    >>> percentage(1, 4)
    25.0
    >>> percentage(2, 3, 1)
    66.7
    """
    if whole == 0:
        return 0.0
    return round(part / whole * 100, ndigits)


def running_total(numbers: Sequence[float]) -> List[float]:
    """Return the cumulative sum at each position as a new list.

    >>> running_total([1, 2, 3, 4])
    [1, 3, 6, 10]
    """
    total: float = 0
    result: List[float] = []
    for n in numbers:
        total += n
        result.append(total)
    return result
