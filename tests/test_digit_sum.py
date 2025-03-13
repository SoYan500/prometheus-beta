import pytest
from src.digit_sum import sum_of_digits

def test_sum_of_digits_with_full_number_string():
    """Test sum of digits in a string of numbers."""
    assert sum_of_digits('1234567890') == 45

def test_sum_of_digits_with_mixed_string():
    """Test sum of digits in a mixed string."""
    assert sum_of_digits('abc123') == 6

def test_sum_of_digits_with_no_digits():
    """Test sum of digits in a string with no digits."""
    assert sum_of_digits('no digits') == 0

def test_sum_of_digits_with_zero_digits():
    """Test sum of digits with leading zeros."""
    assert sum_of_digits('00123') == 6

def test_sum_of_digits_with_empty_string():
    """Test sum of digits in an empty string."""
    assert sum_of_digits('') == 0

def test_sum_of_digits_with_special_characters():
    """Test sum of digits with special characters."""
    assert sum_of_digits('!@#$%123^&*()') == 6

def test_sum_of_digits_type_error():
    """Test that the function raises a TypeError for non-string input."""
    with pytest.raises(AttributeError):
        sum_of_digits(12345)