def to_alternating_uppercase(input_string):
    """
    Convert a string to alternating upper case.

    Args:
        input_string (str): The input string to be converted.

    Returns:
        str: A string with alternating uppercase characters.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If the string is empty, return an empty string
    if not input_string:
        return ""
    
    # Convert to alternating uppercase
    return ''.join(
        char.upper() if (sum(1 for c in input_string[:index] if c.isalpha()) % 2 == 0) else char.lower()
        for index, char in enumerate(input_string)
    )