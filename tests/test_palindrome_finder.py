import pytest
from src.palindrome_finder import find_palindrome_substrings

def test_empty_string():
    """Test that an empty string returns an empty list."""
    assert find_palindrome_substrings("") == []

def test_single_char_string():
    """Test a string with a single character."""
    assert find_palindrome_substrings("a") == ["a"]

def test_simple_palindrome():
    """Test a simple palindrome string."""
    assert set(find_palindrome_substrings("abba")) == set(["a", "b", "bb", "abba"])

def test_no_palindrome():
    """Test a string with no palindrome except individual characters."""
    result = find_palindrome_substrings("abc")
    assert set(result) == set(["a", "b", "c"])

def test_mixed_palindromes():
    """Test a string with multiple types of palindromes."""
    result = set(find_palindrome_substrings("racecar"))
    expected = set(["r", "a", "c", "e", "racecar", "aceca", "cec"])
    assert result == expected

def test_repeated_chars():
    """Test a string with repeated characters."""
    result = set(find_palindrome_substrings("aaa"))
    expected = set(["a", "aa", "aaa"])
    assert result == expected

def test_long_string():
    """Test a longer string with multiple palindromes."""
    result = set(find_palindrome_substrings("aabaa"))
    expected = set(["a", "b", "aa", "aba", "aabaa"])
    assert result == expected

def test_return_type():
    """Verify that the function returns a list."""
    result = find_palindrome_substrings("hello")
    assert isinstance(result, list)

def test_sorted_output():
    """Verify that the output is sorted by length."""
    result = find_palindrome_substrings("abba")
    assert result == sorted(result, key=len)