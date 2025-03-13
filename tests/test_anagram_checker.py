import pytest
from src.anagram_checker import anagram_checker

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert anagram_checker("listen", "silent") == True
    assert anagram_checker("rail safety", "fairy tales") == True

def test_non_anagrams():
    """Test words that are not anagrams"""
    assert anagram_checker("hello", "world") == False
    assert anagram_checker("python", "java") == False

def test_case_insensitive():
    """Test that function is case-insensitive"""
    assert anagram_checker("Debit Card", "Bad Credit") == True
    assert anagram_checker("Astronomer", "Moon starer") == True

def test_whitespace_handling():
    """Test handling of whitespace"""
    assert anagram_checker("  listen  ", "silent") == True
    assert anagram_checker("a gentleman", "elegant man") == True

def test_empty_strings():
    """Test empty string scenarios"""
    assert anagram_checker("", "") == True

def test_different_lengths():
    """Test words of different lengths"""
    assert anagram_checker("short", "shorter") == False
    assert anagram_checker("a", "aa") == False

def test_type_error():
    """Test error handling for non-string inputs"""
    with pytest.raises(TypeError):
        anagram_checker(123, "hello")
    
    with pytest.raises(TypeError):
        anagram_checker("hello", None)

def test_repeated_characters():
    """Test anagrams with repeated characters"""
    assert anagram_checker("aab", "baa") == True
    assert anagram_checker("aab", "aba") == True
    assert anagram_checker("aab", "abc") == False