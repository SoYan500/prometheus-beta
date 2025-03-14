import pytest
from src.palindrome_rearrange import can_form_palindrome

def test_can_form_palindrome():
    # Test cases where palindrome rearrangement is possible
    assert can_form_palindrome("tactcoa") == True
    assert can_form_palindrome("racecar") == True
    assert can_form_palindrome("aab") == True
    assert can_form_palindrome("aabb") == True
    assert can_form_palindrome("A man a plan a canal Panama") == True

    # Test cases where palindrome rearrangement is not possible
    assert can_form_palindrome("hello") == False
    assert can_form_palindrome("world") == False
    assert can_form_palindrome("abcdef") == False

    # Edge cases
    assert can_form_palindrome("") == True
    assert can_form_palindrome(" ") == True
    assert can_form_palindrome("a") == True
    assert can_form_palindrome("aabbccc") == False

    # Case insensitivity and whitespace handling
    assert can_form_palindrome("Able was I ere I saw Elba") == True
    assert can_form_palindrome("Was it a car or a cat I saw") == True