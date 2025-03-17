import pytest
from src.merge_sorted_arrays import merge_sorted_arrays

def test_merge_basic_sorted_arrays():
    """Test merging two basic sorted arrays"""
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3, 4, 5, 6]

def test_merge_with_duplicates():
    """Test merging arrays with duplicate values"""
    arr1 = [1, 2, 3, 3]
    arr2 = [2, 3, 4, 5]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 2, 3, 3, 3, 4, 5]

def test_merge_empty_arrays():
    """Test merging with empty arrays"""
    arr1 = []
    arr2 = [1, 2, 3]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3]
    assert merge_sorted_arrays(arr2, arr1) == [1, 2, 3]
    assert merge_sorted_arrays([], []) == []

def test_merge_single_element_arrays():
    """Test merging arrays with single elements"""
    arr1 = [1]
    arr2 = [2]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2]

def test_error_non_list_inputs():
    """Test error handling for non-list inputs"""
    with pytest.raises(TypeError):
        merge_sorted_arrays("not a list", [1, 2, 3])
    with pytest.raises(TypeError):
        merge_sorted_arrays([1, 2, 3], "not a list")

def test_error_unsorted_arrays():
    """Test error handling for unsorted input arrays"""
    with pytest.raises(ValueError):
        merge_sorted_arrays([3, 1, 2], [1, 2, 3])
    with pytest.raises(ValueError):
        merge_sorted_arrays([1, 2, 3], [3, 1, 2])

def test_large_arrays():
    """Test merging larger sorted arrays"""
    arr1 = list(range(0, 100, 2))  # Even numbers
    arr2 = list(range(1, 100, 2))  # Odd numbers
    result = merge_sorted_arrays(arr1, arr2)
    assert result == list(range(100))
    assert len(result) == 100