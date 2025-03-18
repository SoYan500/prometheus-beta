import pytest
from src.string_permutations import generate_unique_permutations

def test_generate_unique_permutations_basic():
    """Test basic string permutations."""
    result = generate_unique_permutations('abc')
    expected = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    assert sorted(result) == expected

def test_generate_unique_permutations_with_duplicates():
    """Test string with duplicate characters."""
    result = generate_unique_permutations('abb')
    expected = ['abb', 'bab', 'bba']
    assert sorted(result) == expected

def test_generate_unique_permutations_single_char():
    """Test single character input."""
    result = generate_unique_permutations('a')
    assert result == ['a']

def test_generate_unique_permutations_empty_string():
    """Test empty string input."""
    result = generate_unique_permutations('')
    assert result == []

def test_generate_unique_permutations_invalid_input():
    """Test invalid input types."""
    with pytest.raises(TypeError):
        generate_unique_permutations(123)
    
    with pytest.raises(TypeError):
        generate_unique_permutations(None)

def test_generate_unique_permutations_order():
    """Verify that output is sorted."""
    result = generate_unique_permutations('cab')
    expected = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    assert result == expected