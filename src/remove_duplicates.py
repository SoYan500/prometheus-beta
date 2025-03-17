def remove_duplicates(input_string):
    """
    Remove duplicate characters from a given string while preserving the original order.

    Args:
        input_string (str): The input string to remove duplicates from.

    Returns:
        str: A string with duplicate characters removed, keeping the first occurrence of each character.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")

    # Use a set to track seen characters while preserving order
    seen_chars = set()
    result = []

    for char in input_string:
        # Convert character to lowercase for duplicate checking
        lower_char = char.lower()
        if lower_char not in seen_chars:
            seen_chars.add(lower_char)
            result.append(char)

    return ''.join(result)