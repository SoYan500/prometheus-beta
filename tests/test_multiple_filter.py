import pytest
from src.multiple_filter import filter_unique_multiples

def test_basic_filter():
    """Test basic functionality of filtering multiples."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
    assert filter_unique_multiples(input_list) == [5, 6, 9, 10]

def test_empty_list():
    """Test filtering an empty list."""
    assert filter_unique_multiples([]) == []

def test_no_matching_multiples():
    """Test list with no matching multiples."""
    assert filter_unique_multiples([1, 2, 4, 7, 11, 13]) == []

def test_all_multiples():
    """Test list with all numbers being multiples."""
    input_list = [3, 5, 6, 9, 10, 12, 15]
    assert filter_unique_multiples(input_list) == [3, 5, 6, 9, 10]

def test_large_numbers():
    """Test with larger numbers."""
    input_list = [30, 45, 60, 75, 90]
    assert filter_unique_multiples(input_list) == [30, 60, 90]

def test_invalid_input():
    """Test invalid input type raises TypeError."""
    with pytest.raises(TypeError):
        filter_unique_multiples("not a list")
    with pytest.raises(TypeError):
        filter_unique_multiples(123)
    with pytest.raises(TypeError):
        filter_unique_multiples(None)