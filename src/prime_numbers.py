def find_primes_up_to_n(n: int) -> list[int]:
    """
    Find all prime numbers from 1 to n using the Sieve of Eratosthenes algorithm.
    
    Args:
        n (int): The upper limit to find prime numbers up to.
    
    Returns:
        list[int]: A sorted list of prime numbers from 1 to n.
    
    Raises:
        ValueError: If n is less than 2.
    """
    if n < 2:
        raise ValueError("Input must be at least 2 to find prime numbers")
    
    # Create a boolean array of n+1 length, initially all set to True
    # Index will represent the number, value will indicate primality
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    # Use Sieve of Eratosthenes to mark non-primes
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark multiples of i as non-prime
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    
    # Collect and return all prime numbers
    return [num for num in range(2, n+1) if is_prime[num]]