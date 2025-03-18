import pytest
from src.string_case_converter import to_alternating_caps

def test_basic_alternating_caps():
    """Test basic alternating caps conversion."""
    assert to_alternating_caps("hello") == "HeLlO"
    assert to_alternating_caps("world") == "WoRlD"

def test_empty_string():
    """Test empty string input."""
    assert to_alternating_caps("") == ""

def test_single_character():
    """Test single character input."""
    assert to_alternating_caps("a") == "A"
    assert to_alternating_caps("b") == "B"

def test_mixed_case_input():
    """Test input with mixed case."""
    assert to_alternating_caps("AbCdEf") == "AbCdEf"

def test_non_alphabetic_characters():
    """Test string with non-alphabetic characters."""
    assert to_alternating_caps("hello 123 world!") == "HeLlO 123 WoRlD!"

def test_unicode_characters():
    """Test unicode characters."""
    assert to_alternating_caps("héllö") == "HéLlÖ"

def test_invalid_input_type():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        to_alternating_caps(123)
    
    with pytest.raises(TypeError):
        to_alternating_caps(None)
    
    with pytest.raises(TypeError):
        to_alternating_caps(["hello"])