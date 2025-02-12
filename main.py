def main():
    """Entry point of the program. Processes the book content and outputs word and character counts for user insight."""
    book_content = get_book_content("./books/frankenstein.txt")
    words_count, chars_count = count_words(book_content), count_chars(book_content)
    sorted_chars_count = sort_chars_count(chars_count)
    for output in [fmt_words_count(words_count), fmt_chars_count(sorted_chars_count)]:
        print(output)


def get_book_content(filepath: str) -> str:
    """Reads the content of a specified book file to enable analysis."""
    with open(filepath) as f:
        return f.read()


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


def sort_chars_count(chars_dict: dict[str, int]) -> dict[str, int]:
    """Sorts character counts in descending order to highlight the most frequently used characters."""
    return dict(sorted(chars_dict.items(), key=lambda item: item[1], reverse=True))


def fmt_words_count(words_count: int) -> str:
    """Formats the word count into a user-friendly message for output."""
    return f"{words_count} words found in the document"


def fmt_chars_count(chars_dict: dict[str, int]) -> str:
    """Formats character counts into a user-friendly message to inform users about character frequency."""
    fmt = ""
    for k, v in chars_dict.items():
        fmt += f"\nThe '{k}' character was found {v} times"
    return fmt


if __name__ == "__main__":
    main()
