def count_a_chars(input_string: str) -> int:
    """
    Count the number of 'a' characters in the input string, ignoring case sensitivity.

    Args:
        input_string (str): The input string to count 'a' characters in.

    Returns:
        int: The number of 'a' characters in the string (case-insensitive).

    Examples:
        >>> count_a_chars("Apple")
        1
        >>> count_a_chars("banana")
        3
        >>> count_a_chars("AMAZING")
        2
        >>> count_a_chars("")
        0
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return input_string.lower().count('a')