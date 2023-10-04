import re
from hypothesis import given, strategies as st

import utils


def test_read_file(temp_test_file):
    content = utils.read_file(temp_test_file)
    assert content == "This is a test.\nThis is another test.\n"


@given(st.text())
def test_count_bytes(text):
    assert len(text.encode("utf-8")) == utils.count_bytes(text)


@given(st.text())
def test_count_lines(text):
    assert len(text.splitlines()) == utils.count_lines(text)


@given(st.text())
def test_count_words(text):
    assert len(re.split(r"\s+", text.strip())) == utils.count_words(text)


@given(st.text())
def test_count_characters(text):
    assert len(text) == utils.count_characters(text)
