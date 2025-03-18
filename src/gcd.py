def euclidean_gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.

    The Euclidean algorithm works by repeatedly dividing the larger number by the smaller 
    number and replacing the larger number with the remainder until the remainder is zero.

    Args:
        a (int): First integer 
        b (int): Second integer

    Returns:
        int: The greatest common divisor of a and b

    Raises:
        ValueError: If either input is negative
        TypeError: If inputs are not integers
    """
    # Validate input types
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    
    # Validate non-negative inputs
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    # Handle special cases
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Apply Euclidean algorithm
    while b:
        a, b = b, a % b
    
    return a