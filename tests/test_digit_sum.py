import pytest
from src.digit_sum import sum_digits

def test_sum_digits_positive_number():
    """Test sum of digits for a positive number."""
    assert sum_digits(123) == 6
    assert sum_digits(9) == 9
    assert sum_digits(10) == 1

def test_sum_digits_zero():
    """Test sum of digits for zero."""
    assert sum_digits(0) == 0

def test_sum_digits_large_number():
    """Test sum of digits for a large number."""
    assert sum_digits(9876543210) == 45

def test_sum_digits_invalid_input():
    """Test error handling for invalid inputs."""
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits("123")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits(3.14)
    
    # Test negative input
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        sum_digits(-123)