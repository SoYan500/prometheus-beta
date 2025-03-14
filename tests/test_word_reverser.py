import pytest
from src.word_reverser import reverse_words_and_chars

def test_reverse_words_and_chars():
    # Test standard case with multiple words
    assert reverse_words_and_chars("Hello World Python") == "nohtyP dlroW olleH"
    
    # Test single word
    assert reverse_words_and_chars("Hello") == "olleH"
    
    # Test empty string
    assert reverse_words_and_chars("") == ""
    
    # Test string with extra spaces
    assert reverse_words_and_chars("  Hello   World  ") == "dlroW olleH"
    
    # Test special characters and numbers (preserving character order within words)
    assert reverse_words_and_chars("123 abc! def@") == "@fed !cba 321"

def test_input_types():
    # Test with non-string input
    with pytest.raises(AttributeError):
        reverse_words_and_chars(None)
    with pytest.raises(AttributeError):
        reverse_words_and_chars(123)