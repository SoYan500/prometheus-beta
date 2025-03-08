import pytest
from src.palindrome_substrings import find_shortest_palindrome_substrings

def test_basic_palindromes():
    """Test basic palindromic substring extraction"""
    result = find_shortest_palindrome_substrings("abba")
    assert set(result) == {'a', 'b', 'bb', 'abba'}

def test_no_palindromes_longer_than_one():
    """Test when only single-character palindromes exist"""
    assert set(find_shortest_palindrome_substrings("abc")) == {'a', 'b', 'c'}

def test_empty_string():
    """Test handling of empty string"""
    assert find_shortest_palindrome_substrings("") == []

def test_single_character():
    """Test single character input"""
    assert find_shortest_palindrome_substrings("x") == ['x']

def test_all_same_characters():
    """Test string with all same characters"""
    result = find_shortest_palindrome_substrings("aaaa")
    assert set(result) == {'a', 'aa', 'aaa', 'aaaa'}

def test_mixed_palindromes():
    """Test string with multiple length palindromes"""
    result = find_shortest_palindrome_substrings("racecar")
    assert set(result) == {'r', 'a', 'c', 'e', 'racecar'}

def test_complex_palindromes():
    """Test a more complex scenario"""
    result = find_shortest_palindrome_substrings("abbacca")
    assert set(result) == {'a', 'b', 'c'}

def test_sorted_output():
    """Ensure output is sorted"""
    result = find_shortest_palindrome_substrings("abba")
    assert result == sorted(result)