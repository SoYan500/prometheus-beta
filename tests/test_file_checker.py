import os
import pytest
from src.file_checker import file_exists

def test_file_exists_valid_file(tmp_path):
    """Test that function returns True for an existing file."""
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    assert file_exists(str(test_file)) is True

def test_file_exists_nonexistent_file(tmp_path):
    """Test that function returns False for a non-existent file."""
    non_existent_file = tmp_path / "nonexistent.txt"
    assert file_exists(str(non_existent_file)) is False

def test_file_exists_directory(tmp_path):
    """Test that function returns False for a directory."""
    assert file_exists(str(tmp_path)) is False

def test_file_exists_invalid_input():
    """Test that function raises TypeError for non-string inputs."""
    with pytest.raises(TypeError, match="File path must be a string"):
        file_exists(123)
    with pytest.raises(TypeError, match="File path must be a string"):
        file_exists(None)

def test_file_exists_empty_string():
    """Test behavior with an empty string path."""
    assert file_exists("") is False

def test_file_exists_whitespace_string():
    """Test behavior with whitespace-only string path."""
    assert file_exists("   ") is False