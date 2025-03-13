import pytest
from src.multi_array_manipulator import multiArrayManipulator

def test_scalar_multiply():
    """Test multiplication by a scalar."""
    arr = [[1, 2], [3, 4]]
    result = multiArrayManipulator(arr, {'multiply': 2})
    assert result == [[2, 4], [6, 8]]

def test_matrix_multiply():
    """Test multiplication by a matrix."""
    arr = [[1, 2], [3, 4]]
    multiply_matrix = [[1, 0], [0, 1]]
    result = multiArrayManipulator(arr, {'multiply': multiply_matrix})
    assert result == [[1, 2], [3, 4]]

def test_scalar_add():
    """Test addition of a scalar."""
    arr = [[1, 2], [3, 4]]
    result = multiArrayManipulator(arr, {'add': 2})
    assert result == [[3, 4], [5, 6]]

def test_matrix_add():
    """Test addition of a matrix."""
    arr = [[1, 2], [3, 4]]
    add_matrix = [[1, 1], [1, 1]]
    result = multiArrayManipulator(arr, {'add': add_matrix})
    assert result == [[2, 3], [4, 5]]

def test_transpose():
    """Test array transposition."""
    arr = [[1, 2], [3, 4]]
    result = multiArrayManipulator(arr, {'transpose': True})
    assert result == [[1, 3], [2, 4]]

def test_multiple_operations():
    """Test multiple operations in sequence."""
    arr = [[1, 2], [3, 4]]
    result = multiArrayManipulator(arr, {
        'multiply': 2,
        'add': 1,
        'transpose': True
    })
    assert result == [[3, 7], [5, 9]]

def test_invalid_input_type():
    """Test handling of invalid input types."""
    with pytest.raises(ValueError):
        multiArrayManipulator("not an array", {})
    
    with pytest.raises(ValueError):
        multiArrayManipulator([[1, 2], 3], {})

def test_incompatible_multiply_matrix():
    """Test incompatible matrix multiplication."""
    arr = [[1, 2], [3, 4]]
    with pytest.raises(ValueError):
        multiArrayManipulator(arr, {'multiply': [[1], [2]]})

def test_incompatible_add_matrix():
    """Test incompatible matrix addition."""
    arr = [[1, 2], [3, 4]]
    with pytest.raises(ValueError):
        multiArrayManipulator(arr, {'add': [[1, 2, 3], [4, 5, 6]]})