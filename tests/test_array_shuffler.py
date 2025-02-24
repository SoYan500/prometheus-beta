import pytest
import random
from src.array_shuffler import shuffle_array

def test_shuffle_array_basic():
    """Test basic shuffling of a list."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    # Check that the shuffled list contains the same elements
    assert set(shuffled) == set(original)
    
    # Check that the order is different (with high probability)
    assert shuffled != original

def test_shuffle_array_empty():
    """Test shuffling an empty list."""
    assert shuffle_array([]) == []

def test_shuffle_array_single_element():
    """Test shuffling a list with a single element."""
    single_list = [42]
    assert shuffle_array(single_list) == single_list

def test_shuffle_array_different_types():
    """Test shuffling a list with different types of elements."""
    mixed_list = [1, 'a', True, 3.14, None]
    shuffled = shuffle_array(mixed_list)
    
    # Check that the shuffled list contains the same elements
    assert set(shuffled) == set(mixed_list)
    
    # Check that the order is different (with high probability)
    assert shuffled != mixed_list

def test_shuffle_array_invalid_input():
    """Test that TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError):
        shuffle_array("not a list")
    
    with pytest.raises(TypeError):
        shuffle_array(123)

def test_shuffle_randomness():
    """Test that multiple shuffles produce different orders."""
    # Set a fixed seed for reproducibility
    random.seed(42)
    
    original = list(range(10))
    
    # Perform multiple shuffles
    shuffles = [shuffle_array(original) for _ in range(5)]
    
    # Ensure that not all shuffles are the same
    assert len(set(tuple(shuffle) for shuffle in shuffles)) > 1