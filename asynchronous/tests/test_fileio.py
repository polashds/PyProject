import pytest
import unittest
 
from pathlib import Path
from file_io_v4_logfile import read_file_async, BASE_DIR  # adjust if BASE_DIR is inside config.py

@pytest.mark.asyncio
async def test_read_file(tmp_path):
    # Arrange: create a temporary file
    test_file = tmp_path / "sample.csv"
    test_file.write_text("hello,world")

    # Act: call your async function
    content = await read_file_async(test_file.name)

    # Assert: verify file content
    assert "hello,world" in content

@pytest.mark.asyncio
async def test_file_not_found():
    # Act: try reading a non-existing file
    content = await read_file_async("non_existent.csv")

    # Assert: should return empty string
    assert content == ""
