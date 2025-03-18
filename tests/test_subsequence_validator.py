import pytest
from src.subsequence_validator import can_divide_subsequences

def test_valid_vowel_subsequences():
    """Test strings that can be divided into vowel subsequences."""
    assert can_divide_subsequences("aeiou") == True
    assert can_divide_subsequences("aaiioouuee") == True

def test_valid_consonant_subsequences():
    """Test strings that can be divided into consonant subsequences."""
    assert can_divide_subsequences("bcd") == True
    assert can_divide_subsequences("bccddffg") == True

def test_mixed_valid_subsequences():
    """Test strings with mixed valid subsequences."""
    assert can_divide_subsequences("bcaaeiou") == True
    assert can_divide_subsequences("bbaaaiiiooouuu") == True

def test_invalid_subsequences():
    """Test strings that cannot be divided into valid subsequences."""
    assert can_divide_subsequences("abc") == False  # Cannot divide
    assert can_divide_subsequences("aabcc") == False  # Overlapping subsequences
    assert can_divide_subsequences("xyx") == False  # Cannot divide
    assert can_divide_subsequences("bbaa") == False  # Same type subsequences

def test_edge_cases():
    """Test edge case scenarios."""
    # Empty string
    assert can_divide_subsequences("") == False
    
    # Single character
    assert can_divide_subsequences("a") == False
    assert can_divide_subsequences("b") == False

def test_invalid_input():
    """Test inputs with invalid characters."""
    # Non-lowercase letters
    assert can_divide_subsequences("ABC") == False
    assert can_divide_subsequences("aA") == False
    
    # Numbers or special characters
    assert can_divide_subsequences("123") == False
    assert can_divide_subsequences("a1b") == False
    assert can_divide_subsequences("!@#") == False