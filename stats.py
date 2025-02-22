def count_words(book_content: str) -> int:
    """Counts the number of words in the book content to provide a measure of text length."""
    words = book_content.split()
    return len(words)


def count_chars(book_content: str) -> dict[str, int]:
    """Counts the frequency of each character in the book content to analyze character usage."""
    chars_dict = {}
    for char in book_content.lower():
        if char != "\n":
            try:
                if char.isalpha():
                    chars_dict[char] += 1
            except KeyError:
                chars_dict[char] = 1
    return chars_dict
