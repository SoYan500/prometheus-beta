import pytest
from src.max_subarray_sum import max_subarray_sum

def test_basic_positive_array():
    """Test with a simple array of positive and negative numbers."""
    assert max_subarray_sum([1, -2, 3, 4, -1, 5]) == 11

def test_all_negative_array():
    """Test an array with all negative numbers."""
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_all_positive_array():
    """Test an array with all positive numbers."""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_single_element_array():
    """Test an array with a single element."""
    assert max_subarray_sum([42]) == 42

def test_zero_sum_array():
    """Test an array that can have zero as the max sum."""
    assert max_subarray_sum([1, -1, 2, -2]) == 2

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum("not a list")
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum(123)

def test_empty_list():
    """Test that a ValueError is raised for an empty list."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_subarray_sum([])