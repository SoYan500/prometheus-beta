import pytest
from src.palindrome_validator import is_palindrome

def test_valid_palindromes():
    # Test classic palindromes with punctuation and spaces
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    
def test_edge_cases():
    # Empty string
    assert is_palindrome("") == True
    
    # Single character
    assert is_palindrome("a") == True
    
    # Case insensitivity
    assert is_palindrome("Able was I ere I saw Elba") == True
    
def test_numeric_palindromes():
    # Numeric palindromes
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    
def test_special_cases():
    # Strings with only special characters
    assert is_palindrome("!@#$%^&*()") == True
    
    # Mixed alphanumeric with special characters
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b22b2a") == False

def test_whitespace_handling():
    # Various whitespace scenarios
    assert is_palindrome("   madam   ") == True
    assert is_palindrome(" ") == True