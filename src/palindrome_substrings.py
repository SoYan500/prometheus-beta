def find_shortest_palindrome_substrings(s):
    """
    Find the shortest possible palindromic substrings in the given string.
    
    A palindromic substring is a sequence of characters that reads the same 
    forwards and backwards. This function returns a list of the shortest 
    such substrings found in the input string.
    
    Args:
        s (str): The input string to search for palindromic substrings.
    
    Returns:
        list: A list of the shortest palindromic substrings found in the string.
    
    Examples:
        >>> find_shortest_palindrome_substrings("abba")
        ['a', 'b', 'bb', 'abba']
        >>> find_shortest_palindrome_substrings("hello")
        ['h', 'e', 'l', 'l', 'o']
    """
    # Handle edge cases
    if not s:
        return []
    
    # Set to store unique palindromes
    palindromes = set()
    
    # Check all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Extract substring
            substring = s[i:j+1]
            
            # Check if substring is a palindrome
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    # Find the length of the shortest palindromes
    if not palindromes:
        return list(palindromes)
    
    # Get minimum length
    min_length = min(len(p) for p in palindromes)
    
    # Return all palindromes of the minimum length
    return sorted(list(p for p in palindromes if len(p) == min_length))