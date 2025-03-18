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
    
    # Convert to alternating uppercase, tracking alphanumeric characters
    result = []
    uppercase_toggle = True
    for char in input_string:
        if char.isalpha():
            result.append(char.upper() if uppercase_toggle else char.lower())
            uppercase_toggle = not uppercase_toggle
        else:
            result.append(char)
    
    return ''.join(result)