import re


def read_file(path, as_bytes=False):
    mode = "rb" if as_bytes else "r"
    text = ""
    with open(path, mode) as file:
        for line in file:
            text += line
    return text


def count_bytes(text: str):
    """Returns number of bytes in file i.e. wc -c path"""
    return len(text.encode("utf-8"))


def count_lines(text: str):
    """Returns number of lines in file i.e. wc -l path"""
    return len(text.splitlines())


def count_words(text: str):
    """Returns number of words in file i.e. wc -w path"""
    return len(re.split(r"\s+", text.strip()))


def count_characters(text: str):
    """Returns number of characters in file i.e. wc -m path"""
    return len(text)
