import pytest
from src.gcd import euclidean_gcd

def test_gcd_basic_cases():
    """Test common GCD scenarios"""
    assert euclidean_gcd(48, 18) == 6
    assert euclidean_gcd(54, 24) == 6
    assert euclidean_gcd(17, 23) == 1
    assert euclidean_gcd(0, 5) == 5
    assert euclidean_gcd(5, 0) == 5

def test_gcd_same_number():
    """Test when both inputs are the same"""
    assert euclidean_gcd(7, 7) == 7
    assert euclidean_gcd(0, 0) == 0

def test_gcd_one_is_multiple():
    """Test when one number is a multiple of the other"""
    assert euclidean_gcd(12, 3) == 3
    assert euclidean_gcd(3, 12) == 3

def test_gcd_large_numbers():
    """Test with larger numbers"""
    assert euclidean_gcd(1071, 462) == 21
    assert euclidean_gcd(462, 1071) == 21

def test_gcd_negative_input_error():
    """Test that negative inputs raise ValueError"""
    with pytest.raises(ValueError):
        euclidean_gcd(-10, 5)
    with pytest.raises(ValueError):
        euclidean_gcd(10, -5)
    with pytest.raises(ValueError):
        euclidean_gcd(-10, -5)

def test_gcd_non_integer_error():
    """Test that non-integer inputs raise TypeError"""
    with pytest.raises(TypeError):
        euclidean_gcd(10.5, 5)
    with pytest.raises(TypeError):
        euclidean_gcd(10, 5.5)
    with pytest.raises(TypeError):
        euclidean_gcd("10", 5)
    with pytest.raises(TypeError):
        euclidean_gcd(10, "5")