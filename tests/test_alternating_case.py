import pytest
from src.alternating_case import to_alternating_uppercase

def test_basic_alternating_uppercase():
    """Test basic string conversion to alternating uppercase."""
    assert to_alternating_uppercase("hello") == "HeLlO"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_alternating_uppercase("") == ""

def test_single_character():
    """Test conversion of a single character."""
    assert to_alternating_uppercase("a") == "A"

def test_mixed_case_input():
    """Test conversion with mixed case input."""
    assert to_alternating_uppercase("PytHOn") == "PyThOn"

def test_string_with_spaces():
    """Test conversion of a string with spaces."""
    assert to_alternating_uppercase("hello world") == "HeLlO WoRlD"

def test_string_with_special_characters():
    """Test conversion of a string with special characters."""
    assert to_alternating_uppercase("hello, world!") == "HeLlO, WoRlD!"

def test_non_string_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_uppercase(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_uppercase(None)

def test_unicode_characters():
    """Test conversion with unicode characters."""
    assert to_alternating_uppercase("café") == "CaFé"