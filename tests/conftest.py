import pytest

CONTENT = "This is a test.\nThis is another test.\n"


@pytest.fixture
def temp_test_file(tmpdir):
    file_path = tmpdir.join("temp_test_file.txt")
    file_path.write_text(CONTENT, encoding="utf-8")
    yield file_path
