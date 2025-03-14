import pytest
from src.count_a_chars import count_a_chars

def test_count_a_chars_basic():
    """Test basic functionality of counting 'a' characters."""
    assert count_a_chars("Apple") == 1
    assert count_a_chars("banana") == 3
    assert count_a_chars("AMAZING") == 2
    assert count_a_chars("") == 0

def test_count_a_chars_case_insensitive():
    """Test case insensitivity."""
    assert count_a_chars("aAaAaA") == 6
    assert count_a_chars("AbracAdabra") == 5

def test_count_a_chars_no_as():
    """Test string with no 'a' characters."""
    assert count_a_chars("hello") == 0
    assert count_a_chars("WORLD") == 0

def test_count_a_chars_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_a_chars(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        count_a_chars(None)
    with pytest.raises(TypeError, match="Input must be a string"):
        count_a_chars(["a", "b", "c"])