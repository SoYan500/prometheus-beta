def filter_unique_multiples(numbers):
    """
    Filter a list of integers to return multiples of 3 or 5, but not both, sorted in ascending order.

    Args:
        numbers (list): A list of integers to filter.

    Returns:
        list: A sorted list of integers that are multiples of 3 or 5, but not both.

    Examples:
        >>> filter_unique_multiples([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15])
        [5, 6, 9, 10]
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers")
    
    # Filter numbers that are multiples of 3 or 5, but not both
    unique_multiples = [
        num for num in numbers 
        if ((num % 3 == 0) ^ (num % 5 == 0))
    ]
    
    # Return sorted list
    return sorted(unique_multiples)