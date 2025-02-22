import sys
from stats import count_words, count_chars
from format import sort_chars_count, fmt_words_count, fmt_chars_count
from book_io import get_book_arg, get_book_content


def main():
    """Entry point of the program. Processes the book content and outputs word and character counts for user insight."""
    book_path = get_book_arg(sys.argv)
    book_content = get_book_content(book_path)
    words_count, chars_count = count_words(book_content), count_chars(book_content)
    sorted_chars_count = sort_chars_count(chars_count)
    for output in [fmt_words_count(words_count), fmt_chars_count(sorted_chars_count)]:
        print(output)


if __name__ == "__main__":
    main()
