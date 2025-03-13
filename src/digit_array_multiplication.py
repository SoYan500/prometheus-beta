def multiply_digit_arrays(A, B):
    """
    Multiply two arrays of digits and return the result as an array of digits.
    
    Args:
        A (list): First array of digits
        B (list): Second array of digits of the same length
    
    Returns:
        list: Result of multiplication represented as an array of digits
    
    Raises:
        ValueError: If arrays are not of equal length or contain non-integer values
    """
    # Validate input
    if len(A) != len(B):
        raise ValueError("Input arrays must be of equal length")
    
    # Validate all elements are single digits
    if not all(isinstance(digit, int) and 0 <= digit <= 9 for digit in A + B):
        raise ValueError("All array elements must be single digits (0-9)")
    
    # Convert arrays to integers
    num_a = int(''.join(map(str, A)))
    num_b = int(''.join(map(str, B)))
    
    # Multiply and convert result back to digit array
    result = num_a * num_b
    
    # Convert result to array of digits
    return [int(d) for d in str(result)]