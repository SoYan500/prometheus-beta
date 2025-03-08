import pytest
from src.palindrome_substrings import find_shortest_palindrome_substrings

def test_basic_palindromes():
    """Test basic palindromic substring extraction"""
    result = find_shortest_palindrome_substrings("abba")
    assert len(result) == 4
    assert 'a' in result
    assert 'b' in result
    assert 'bb' in result
    assert 'abba' in result

def test_no_palindromes_longer_than_one():
    """Test when only single-character palindromes exist"""
    result = find_shortest_palindrome_substrings("abc")
    assert set(result) == {'a', 'b', 'c'}

def test_empty_string():
    """Test handling of empty string"""
    assert find_shortest_palindrome_substrings("") == []

def test_single_character():
    """Test single character input"""
    assert find_shortest_palindrome_substrings("x") == ['x']

def test_all_same_characters():
    """Test string with all same characters"""
    result = find_shortest_palindrome_substrings("aaaa")
    assert len(result) == 4
    assert 'a' in result
    assert 'aa' in result
    assert 'aaa' in result
    assert 'aaaa' in result

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