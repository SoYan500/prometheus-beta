import pytest
from src.digit_array_multiplication import multiply_digit_arrays

def test_basic_multiplication():
    """Test basic multiplication of digit arrays"""
    A = [1, 2, 3]  # 123
    B = [4, 5, 6]  # 456
    assert multiply_digit_arrays(A, B) == [5, 6, 0, 8, 8]

def test_zero_multiplication():
    """Test multiplication involving zero"""
    A = [0, 0, 5]  # 5
    B = [1, 2, 0]  # 120
    assert multiply_digit_arrays(A, B) == [0, 6, 0]

def test_single_digit_arrays():
    """Test multiplication of single-digit arrays"""
    A = [7]
    B = [8]
    assert multiply_digit_arrays(A, B) == [5, 6]

def test_unequal_length_arrays():
    """Test that an error is raised for unequal length arrays"""
    with pytest.raises(ValueError, match="Input arrays must be of equal length"):
        multiply_digit_arrays([1, 2], [3, 4, 5])

def test_invalid_digit_input():
    """Test that an error is raised for non-digit inputs"""
    with pytest.raises(ValueError, match="All array elements must be single digits"):
        multiply_digit_arrays([1, 10], [2, 3])

def test_large_number_multiplication():
    """Test multiplication of larger numbers"""
    A = [9, 9, 9]  # 999
    B = [9, 9, 9]  # 999
    assert multiply_digit_arrays(A, B) == [9, 9, 8, 0, 0, 1]