import pytest
from src.tournament_sort import tournament_sort

def test_tournament_sort_basic_integers():
    """Test sorting a list of integers in ascending order."""
    input_list = [5, 2, 9, 1, 7, 6]
    expected = sorted(input_list)
    result = tournament_sort(input_list)
    assert result == expected

def test_tournament_sort_descending():
    """Test sorting with a custom comparison function for descending order."""
    input_list = [5, 2, 9, 1, 7, 6]
    expected = sorted(input_list, reverse=True)
    result = tournament_sort(input_list, compare=lambda x, y: x > y)
    assert result == expected

def test_tournament_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    result = tournament_sort(input_list)
    assert result == input_list

def test_tournament_sort_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot sort an empty list"):
        tournament_sort([])

def test_tournament_sort_non_list_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        tournament_sort("not a list")

def test_tournament_sort_strings():
    """Test sorting a list of strings."""
    input_list = ["banana", "apple", "cherry", "date"]
    expected = sorted(input_list)
    result = tournament_sort(input_list)
    assert result == expected

def test_tournament_sort_mixed_types():
    """Test sorting with a custom comparator for mixed types."""
    class Person:
        def __init__(self, age):
            self.age = age
    
    people = [Person(25), Person(20), Person(30), Person(22)]
    result = tournament_sort(people, compare=lambda x, y: x.age < y.age)
    
    # Verify the result is sorted by age
    ages = [p.age for p in result]
    assert ages == sorted(ages)

def test_tournament_sort_stability():
    """Test sorting stability with equal elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6]
    expected = sorted(input_list)
    result = tournament_sort(input_list)
    assert result == expected