import os
import pytest


@pytest.fixture
def temp_test_file(tmpdir):
    file_path = tmpdir.join("temp_test_file.txt")
    with open(file_path, "w") as temp_file:
        temp_file.write("This is a test.\nThis is another test.\n")
    yield file_path
    os.remove(file_path)
