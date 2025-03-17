import pytest
from src.prime_numbers import find_primes_up_to_n

def test_primes_up_to_10():
    """Test prime numbers up to 10."""
    expected_primes = [2, 3, 5, 7]
    assert find_primes_up_to_n(10) == expected_primes

def test_primes_up_to_100():
    """Test prime numbers up to 100."""
    expected_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
        53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    ]
    assert find_primes_up_to_n(100) == expected_primes

def test_prime_lower_bound():
    """Test that ValueError is raised for inputs less than 2."""
    with pytest.raises(ValueError, match="Input must be at least 2 to find prime numbers"):
        find_primes_up_to_n(1)

def test_prime_zero():
    """Test that ValueError is raised for zero."""
    with pytest.raises(ValueError, match="Input must be at least 2 to find prime numbers"):
        find_primes_up_to_n(0)

def test_negative_input():
    """Test that ValueError is raised for negative inputs."""
    with pytest.raises(ValueError, match="Input must be at least 2 to find prime numbers"):
        find_primes_up_to_n(-5)

def test_edge_case_2():
    """Test handling of the lowest prime number, 2."""
    assert find_primes_up_to_n(2) == [2]