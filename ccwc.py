import argparse
import sys

from utils import count_bytes, count_characters, count_lines, count_words, read_file


def main():
    parser = argparse.ArgumentParser(
        prog="ccwc",
        description="""ccwc utility displays the number of lines, words, and bytes contained in each input file, or standard input (if
        no file is specified) to the standard output.""",
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "-c",
        "--bytes",
        action="store_true",
        help="The number of bytes in each input file is written to the standard output.  This will cancel out any prior usage of the -m option.",
    )
    group.add_argument(
        "-l",
        "--lines",
        action="store_true",
        help="The number of lines in each input file is written to the standard output.",
    )
    group.add_argument(
        "-m",
        "--chars",
        action="store_true",
        help="The number of characters in each input file is written to the standard output. "
        "If the current locale does not support multibyte characters, this is equivalent to the -c option."
        "This will cancel out any prior usage of the -c option.",
    )
    group.add_argument(
        "-w",
        "--words",
        action="store_true",
        help="The number of words in each input file is written to the standard output.",
    )
    parser.add_argument(
        "path", nargs="?", type=str, help="path to input file or standard input"
    )
    args = parser.parse_args()

    # Read input based on whether a file path is provided or not
    if args.path:
        text = read_file(args.path)
        path = args.path
    else:
        text = sys.stdin.read()
        path = ""

    # Determine the count based on the specified options
    count_function = {
        args.bytes: count_bytes,
        args.lines: count_lines,
        args.chars: count_characters,
        args.words: count_words,
    }.get(True, lambda x: f"{count_lines(x)} {count_words(x)} {count_bytes(x)}")

    out = count_function(text)

    print(f"{out} {path}")


if __name__ == "__main__":
    sys.exit(main())
