import re


def count_bytes(path: str):
    """Returns number of bytes in file i.e. wc -c path"""
    with open(path, "rb") as f:
        result = f.read()
    return len(result)


def count_lines(path: str):
    """Returns number of lines in file i.e. wc -l path"""
    with open(path, "r") as f:
        result = f.readlines()
    return len(result)


def count_words(path: str):
    """Returns number of words in file i.e. wc -w path"""
    with open(path, "r") as f:
        text = f.read().strip()
    result = re.split("\s+", text)  # noqa
    return len(result)


def count_characters(path: str):
    """Returns number of characters in file i.e. wc -m path"""
    with open(path, "r") as f:
        result = f.read()
    return len(result)
