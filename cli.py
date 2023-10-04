import argparse

from utils import count_bytes, count_characters, count_lines, count_words

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
parser.add_argument("path", type=str, help="path to input file or standard input")
args = parser.parse_args()

path = args.path

if args.bytes:
    out = count_bytes(path)

elif args.lines:
    out = count_lines(path)

elif args.chars:
    out = count_characters(path)

elif args.words:
    out = count_words(path)

else:
    out = f"{count_lines(path)}  {count_words(path)}  {count_bytes(path)}"


print(out, path)
