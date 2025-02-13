# py-bookbot

## Requirements

Ensure that Python is installed on your system. You can check your installed version with:

```
python --version
```

If you need to install Python, [download the latest version](https://www.python.org/downloads/).

## Installation

```
git clone https://github.com/alnah/py-bookbot && cd py-bookbot
```

## Usage

Download a book, and save it as a `.txt` file. For example:

```
curl -o books/frankenstein.txt https://www.gutenberg.org/files/84/84-0.txt
```

Open `main.py` with your text editor, and update:

```python
 book_path = "./books/frankenstein.txt"
```

Run the script:

```
python run main.py
```
