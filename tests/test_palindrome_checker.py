import pytest
from src.palindrome_checker import is_palindrome

def test_palindrome_basic():
    """Test basic palindrome cases"""
    assert is_palindrome([1, 2, 1]) == True
    assert is_palindrome([1, 2, 3]) == False

def test_palindrome_empty_and_single():
    """Test empty list and single-element list"""
    assert is_palindrome([]) == True
    assert is_palindrome([42]) == True

def test_palindrome_even_length():
    """Test palindromes with even length"""
    assert is_palindrome([1, 2, 2, 1]) == True
    assert is_palindrome([1, 2, 3, 4]) == False

def test_palindrome_longer_list():
    """Test longer palindrome lists"""
    assert is_palindrome([1, 2, 3, 3, 2, 1]) == True
    assert is_palindrome([1, 2, 3, 4, 5, 6]) == False

def test_palindrome_type_error():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        is_palindrome("not a list")
    with pytest.raises(TypeError):
        is_palindrome(123)
    with pytest.raises(TypeError):
        is_palindrome(None)