def reverse_words_and_chars(input_string):
    """
    Reverse the order of words in a string and the characters within each word.
    
    Args:
        input_string (str): The input string to be processed.
    
    Returns:
        str: A string with words in reverse order and characters of each word reversed.
    
    Examples:
        >>> reverse_words_and_chars("Hello World Python")
        'nohtyP dlroW olleH'
        >>> reverse_words_and_chars("")
        ''
        >>> reverse_words_and_chars("SingleWord")
        'droWelgniS'
    """
    # Handle empty string case
    if not input_string:
        return ""
    
    # Split the string into words, reverse the order of words
    words = input_string.split()
    
    # Reverse characters in each word and then reverse the word order
    reversed_words = [word[::-1] for word in words][::-1]
    
    # Join the reversed words back into a string
    return " ".join(reversed_words)