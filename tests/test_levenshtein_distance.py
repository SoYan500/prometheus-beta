import pytest
from src.levenshtein_distance import levenshtein_distance

def test_identical_strings():
    """Test distance between identical strings is zero"""
    assert levenshtein_distance("hello", "hello") == 0

def test_empty_strings():
    """Test distance between empty strings"""
    assert levenshtein_distance("", "") == 0

def test_one_empty_string():
    """Test distance when one string is empty"""
    assert levenshtein_distance("hello", "") == 5
    assert levenshtein_distance("", "world") == 5

def test_simple_edits():
    """Test basic edit scenarios"""
    assert levenshtein_distance("kitten", "sitting") == 3
    assert levenshtein_distance("sunday", "saturday") == 3

def test_different_length_strings():
    """Test strings of different lengths"""
    assert levenshtein_distance("short", "shorter") == 2
    assert levenshtein_distance("longer", "long") == 2

def test_complete_transformation():
    """Test transforming one string completely into another"""
    assert levenshtein_distance("", "abc") == 3
    assert levenshtein_distance("abc", "") == 3

def test_case_sensitivity():
    """Test case sensitivity"""
    assert levenshtein_distance("Hello", "hello") == 1

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        levenshtein_distance(123, "hello")
    with pytest.raises(TypeError):
        levenshtein_distance("hello", [1, 2, 3])
    with pytest.raises(TypeError):
        levenshtein_distance(None, "test")