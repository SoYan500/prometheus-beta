import os
import pytest
import tempfile
import shutil

from src.directory_utils import directory_exists

def test_existing_directory():
    """Test that an existing directory returns True."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert directory_exists(temp_dir) is True

def test_non_existing_directory():
    """Test that a non-existing directory returns False."""
    non_existing_path = "/path/to/definitely/non/existing/directory"
    assert directory_exists(non_existing_path) is False

def test_file_path():
    """Test that a file path returns False."""
    with tempfile.NamedTemporaryFile() as temp_file:
        assert directory_exists(temp_file.name) is False

def test_none_input():
    """Test that None input raises a TypeError."""
    with pytest.raises(TypeError):
        directory_exists(None)

def test_current_directory():
    """Test that the current directory exists."""
    assert directory_exists('.') is True

def test_parent_directory():
    """Test that the parent directory exists."""
    assert directory_exists('..') is True

def test_unicode_path():
    """Test path with unicode characters."""
    with tempfile.TemporaryDirectory(prefix="テスト") as temp_dir:
        assert directory_exists(temp_dir) is True