import pytest
from src.z_algorithm import z_algorithm

def test_basic_string_matching():
    """Test basic string matching scenario"""
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    assert z_algorithm(text, pattern) == [10]

def test_multiple_matches():
    """Test scenario with multiple pattern matches"""
    text = "AAAAAAA"
    pattern = "AA"
    assert z_algorithm(text, pattern) == [0, 1, 2, 3, 4, 5]

def test_no_matches():
    """Test scenario with no matches"""
    text = "ABCDEFG"
    pattern = "XYZ"
    assert z_algorithm(text, pattern) == []

def test_pattern_longer_than_text():
    """Test when pattern is longer than text"""
    text = "ABC"
    pattern = "ABCDEF"
    assert z_algorithm(text, pattern) == []

def test_edge_case_same_text_and_pattern():
    """Test when text and pattern are the same"""
    text = "ABCABC"
    pattern = "ABCABC"
    assert z_algorithm(text, pattern) == [0]

def test_type_error_non_string_inputs():
    """Test error handling for non-string inputs"""
    with pytest.raises(TypeError):
        z_algorithm(123, "pattern")
    with pytest.raises(TypeError):
        z_algorithm("text", 456)

def test_value_error_empty_inputs():
    """Test error handling for empty inputs"""
    with pytest.raises(ValueError):
        z_algorithm("", "pattern")
    with pytest.raises(ValueError):
        z_algorithm("text", "")

def test_case_sensitivity():
    """Test case sensitivity of the algorithm"""
    text = "AbcAbcABC"
    pattern = "abc"
    assert z_algorithm(text, pattern) == []
    
    pattern = "Abc"
    assert z_algorithm(text, pattern) == [0, 3]