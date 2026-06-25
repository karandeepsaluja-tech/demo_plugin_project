"""String utilities — small, pure, dependency-free text helpers.

Every function here is deterministic: same input always gives the same
output, no I/O, no global state. Standard library only.
"""
import re


def slugify(text: str) -> str:
    """Convert a string into a URL-safe slug.

    Lowercases, replaces any run of non-alphanumeric characters with a
    single hyphen, and strips leading/trailing hyphens.

    >>> slugify("Hello, World!")
    'hello-world'
    >>> slugify("  Multiple   Spaces  ")
    'multiple-spaces'
    """
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def truncate_words(text: str, max_words: int, suffix: str = "...") -> str:
    """Truncate text to at most ``max_words`` words, appending ``suffix``.

    If the text already has fewer words than the limit, it is returned
    unchanged (and the suffix is NOT added).

    >>> truncate_words("the quick brown fox jumps", 3)
    'the quick brown...'
    >>> truncate_words("short text", 5)
    'short text'
    """
    words = text.split()
    if len(words) <= max_words:
        return text
    return " ".join(words[:max_words]) + suffix


def normalize_whitespace(text: str) -> str:
    """Collapse all runs of whitespace into single spaces and strip ends.

    >>> normalize_whitespace("  a\\t\\tb\\n c  ")
    'a b c'
    """
    return re.sub(r"\s+", " ", text).strip()


def count_vowels(text: str) -> int:
    """Return the number of vowels (a, e, i, o, u) in the text, case-insensitive.

    >>> count_vowels("Hello World")
    3
    """
    return sum(1 for ch in text.lower() if ch in "aeiou")


def title_case_preserving_acronyms(text: str) -> str:
    """Title-case a string but keep all-uppercase words (acronyms) intact.

    >>> title_case_preserving_acronyms("the json api guide")
    'The Json Api Guide'
    >>> title_case_preserving_acronyms("using HTTP and SQL")
    'Using HTTP And SQL'
    """
    result = []
    for word in text.split():
        if word.isupper() and len(word) > 1:
            result.append(word)
        else:
            result.append(word.capitalize())
    return " ".join(result)
