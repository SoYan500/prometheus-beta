def sum_digits(number):
    """
    Calculate the sum of digits for a given integer.

    Args:
        number (int): The input number whose digits will be summed.

    Returns:
        int: The sum of all digits in the number.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is negative.

    Examples:
        >>> sum_digits(123)
        6
        >>> sum_digits(0)
        0
    """
    # Validate input
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle zero as a special case
    if number == 0:
        return 0
    
    # Convert number to absolute value to handle any potential negative input
    number = abs(number)
    
    # Sum the digits
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10  # Get the last digit
        number //= 10  # Remove the last digit
    
    return digit_sum