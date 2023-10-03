import re


def count_bytes(path: str):
    """Returns number of bytes in file"""
    with open(path, "rb") as f:
        text = f.read()
    return f"{len(text)} {path}"


def count_lines(path: str):
    """Returns number of lines in file"""
    with open(path, "r") as f:
        lines = f.readlines()
    return f"{len(lines)} {path}"


def count_words(path: str):
    """Returns number of words in file"""
    with open(path, "r") as f:
        text = f.read().strip()
    words = re.split("\s+", text)  # noqa
    return f"{len(words)} {path}"


def count_characters(path: str):
    with open(path, "r") as f:
        text = f.read()
    return f"{len(list(text))} {path}"


if __name__ == '__main__':
    print(count_characters("test.txt"))
    # print(list("hello world"))

