from unittest.mock import patch

from ccwc import main


def test_default_count(capsys, temp_test_file):
    with patch("sys.argv", ["ccwc", f"{temp_test_file}"]):
        main()
        captured = capsys.readouterr()
        assert captured.out == f"2 8 38 {temp_test_file}\n"


def test_bytes_count(capsys, temp_test_file):
    with patch("sys.argv", ["ccwc", "-c", f"{temp_test_file}"]):
        main()
        captured = capsys.readouterr()
        assert captured.out == f"38 {temp_test_file}\n"


def test_char_count(capsys, temp_test_file):
    with patch("sys.argv", ["ccwc", "-m", f"{temp_test_file}"]):
        main()
        captured = capsys.readouterr()
        assert captured.out == f"38 {temp_test_file}\n"


def test_word_count(capsys, temp_test_file):
    with patch("sys.argv", ["ccwc", "-w", f"{temp_test_file}"]):
        main()
        captured = capsys.readouterr()
        assert captured.out == f"8 {temp_test_file}\n"


def test_line_count(capsys, temp_test_file):
    with patch("sys.argv", ["ccwc", "-l", f"{temp_test_file}"]):
        main()
        captured = capsys.readouterr()
        assert captured.out == f"2 {temp_test_file}\n"
