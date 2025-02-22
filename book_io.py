import sys


def get_book_content(filepath: str) -> str:
    """Reads the content of a specified book file to enable analysis."""
    with open(filepath) as f:
        return f.read()


def get_book_arg(argv: list[str]) -> str:
    """Retrieve the second argument from the user in stdin."""
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]
