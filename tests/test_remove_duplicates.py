import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic string with duplicate characters."""
    assert remove_duplicates("hello") == "helo"
    assert remove_duplicates("aabbccdd") == "abcd"

def test_remove_duplicates_empty_string():
    """Test handling of an empty string."""
    assert remove_duplicates("") == ""

def test_remove_duplicates_no_duplicates():
    """Test string with no duplicate characters."""
    assert remove_duplicates("python") == "python"

def test_remove_duplicates_mixed_case():
    """Test string with mixed case characters."""
    assert remove_duplicates("HeLLo") == "HeLo"

def test_remove_duplicates_special_chars():
    """Test string with special characters and duplicates."""
    assert remove_duplicates("!@#!@#$%^") == "!@#$%^"

def test_remove_duplicates_error_handling():
    """Test error handling for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicates(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicates(None)