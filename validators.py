"""Validation helpers — pure predicate and parsing functions.

Deterministic, standard-library only. Good examples of small reusable
units the harvester can verify by running them on sample inputs.
"""
import re


def is_valid_email(value):
    """Return True if ``value`` looks like a basic email address.

    This is a pragmatic check (local@domain.tld), not full RFC validation.

    >>> is_valid_email("jane.doe@example.com")
    True
    >>> is_valid_email("not-an-email")
    False
    """
    if not isinstance(value, str):
        return False
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.match(pattern, value) is not None


def is_valid_hex_color(value):
    """Return True if ``value`` is a valid 3- or 6-digit hex color.

    >>> is_valid_hex_color("#fff")
    True
    >>> is_valid_hex_color("#1a2b3c")
    True
    >>> is_valid_hex_color("red")
    False
    """
    if not isinstance(value, str):
        return False
    return re.match(r"^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$", value) is not None


def clamp(value, low, high):
    """Constrain a number to the inclusive range [low, high].

    >>> clamp(15, 0, 10)
    10
    >>> clamp(-3, 0, 10)
    0
    >>> clamp(5, 0, 10)
    5
    """
    if low > high:
        raise ValueError("low must not exceed high")
    return max(low, min(value, high))


def parse_bool(value):
    """Parse a human string into a boolean.

    Accepts (case-insensitive) true/yes/1/on as True and
    false/no/0/off as False. Raises ValueError on anything else.

    >>> parse_bool("YES")
    True
    >>> parse_bool("off")
    False
    """
    s = str(value).strip().lower()
    if s in ("true", "yes", "1", "on"):
        return True
    if s in ("false", "no", "0", "off"):
        return False
    raise ValueError(f"cannot parse boolean from {value!r}")
