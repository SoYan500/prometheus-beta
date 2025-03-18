def to_alternating_caps(input_string):
    """
    Convert a string to alternating caps case.

    Args:
        input_string (str): The input string to convert.

    Returns:
        str: The string converted to alternating caps case.

    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Convert to alternating caps
    return ''.join(
        char.upper() if idx % 2 == 0 else char.lower() 
        for idx, char in enumerate(input_string)
    )