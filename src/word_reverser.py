def reverse_words_and_chars(input_string):
    """
    Reverse the order of words in a string and the characters within each word.
    
    Args:
        input_string (str): The input string to be processed.
    
    Returns:
        str: A string with words in reverse order and characters of each word reversed.
    
    Raises:
        AttributeError: If input is not a string.
    
    Examples:
        >>> reverse_words_and_chars("Hello World Python")
        'nohtyP dlroW olleH'
        >>> reverse_words_and_chars("")
        ''
        >>> reverse_words_and_chars("SingleWord")
        'droWelgniS'
    """
    # Validate input is a string
    if not isinstance(input_string, str):
        raise AttributeError("Input must be a string")
    
    # Handle empty string case
    if not input_string.strip():
        return ""
    
    # Split the string into words, removing extra whitespace
    words = input_string.split()
    
    # Reverse characters in each word and then reverse the word order
    reversed_words = [word[::-1] for word in words][::-1]
    
    # Join the reversed words back into a string
    return " ".join(reversed_words)