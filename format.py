def sort_chars_count(chars_dict: dict[str, int]) -> dict[str, int]:
    """Sorts character counts in descending order to highlight the most frequently used characters."""
    return dict(sorted(chars_dict.items(), key=lambda item: item[1], reverse=True))


def fmt_words_count(words_count: int) -> str:
    """Formats the word count into a user-friendly message for output."""
    return f"Found {words_count} total words"


def fmt_chars_count(chars_dict: dict[str, int]) -> str:
    """Formats character counts into a user-friendly message to inform users about character frequency."""
    fmt = ""
    for k, v in chars_dict.items():
        fmt += f"\n{k}: {v}"
    return fmt
