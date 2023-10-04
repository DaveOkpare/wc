# ccwc - Character, Word, and Byte Count Utility

This utility, named `ccwc`, is designed to provide insights into the number of lines, words, and bytes present in each input file or standard input. Users can specify the desired output, including counts for lines, words, and bytes, to be displayed on the standard output.

This project was completed as part of [John Crickett Coding Challenges.](https://codingchallenges.fyi/challenges/challenge-wc/)

## Usage

```bash
python ccwc.py [-h] [-c | -l | -m | -w] [path]
```

## Arguments
- `path` (optional): Path to the input file or standard input. If not provided, standard input is used.
- `-c`, `--bytes`: Display the number of bytes in each input file.
- `-l`, `--lines`: Display the number of lines in each input file.
- `-m`, `--chars`: Display the number of characters in each input file. If the current locale does not support multibyte characters, this is equivalent to the -c option.
- `-w`, `--words`: Display the number of words in each input file.

## Examples

1. Count bytes in a file:

```bash
python ccwc.py -c path/to/file.txt
```

2. Count lines in a file:

```bash
python ccwc.py -l path/to/file.txt
```

3. Count words in a file:

```bash
python ccwc.py -w path/to/file.txt
```

4. Count characters in a file:

```bash
python ccwc.py -m path/to/file.txt
```

5. Provide input via standard input:

```bash
cat path/to/file.txt | python ccwc.py
```

