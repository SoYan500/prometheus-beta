import pytest
from src.kth_smallest import find_kth_smallest

def test_basic_functionality():
    """Test finding kth smallest in a simple list"""
    arr = [7, 10, 4, 3, 20, 15]
    assert find_kth_smallest(arr, 3) == 7

def test_sorted_list():
    """Test finding kth smallest in an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert find_kth_smallest(arr, 4) == 4

def test_reverse_sorted_list():
    """Test finding kth smallest in a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert find_kth_smallest(arr, 2) == 2

def test_list_with_duplicates():
    """Test finding kth smallest in a list with duplicate elements"""
    arr = [3, 3, 1, 4, 2, 4]
    assert find_kth_smallest(arr, 3) == 3

def test_single_element_list():
    """Test finding kth smallest in a single-element list"""
    arr = [42]
    assert find_kth_smallest(arr, 1) == 42

def test_first_smallest():
    """Test finding the first smallest element"""
    arr = [5, 4, 3, 2, 1]
    assert find_kth_smallest(arr, 1) == 1

def test_last_smallest():
    """Test finding the last (largest) smallest element"""
    arr = [5, 4, 3, 2, 1]
    assert find_kth_smallest(arr, 5) == 5

def test_invalid_k_too_low():
    """Test that ValueError is raised when k is less than 1"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be between 1 and 3"):
        find_kth_smallest(arr, 0)

def test_invalid_k_too_high():
    """Test that ValueError is raised when k is greater than list length"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be between 1 and 3"):
        find_kth_smallest(arr, 4)

def test_empty_list():
    """Test that ValueError is raised for an empty list"""
    arr = []
    with pytest.raises(ValueError, match="Array cannot be empty"):
        find_kth_smallest(arr, 1)

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_kth_smallest("not a list", 1)

def test_invalid_k_type():
    """Test that TypeError is raised for non-integer k"""
    arr = [1, 2, 3]
    with pytest.raises(TypeError, match="k must be an integer"):
        find_kth_smallest(arr, "1")