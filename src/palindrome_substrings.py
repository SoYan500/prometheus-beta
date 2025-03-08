def find_shortest_palindrome_substrings(s):
    """
    Find the shortest possible palindromic substrings in the given string.
    
    A palindromic substring is a sequence of characters that reads the same 
    forwards and backwards. This function returns a list of the shortest 
    such substrings found in the string.
    
    Args:
        s (str): The input string to search for palindromic substrings.
    
    Returns:
        list: A sorted list of the shortest palindromic substrings.
    
    Examples:
        >>> find_shortest_palindrome_substrings("abba")
        ['a', 'b', 'bb', 'abba']
        >>> find_shortest_palindrome_substrings("hello")
        ['h', 'e', 'l', 'l', 'o']
    """
    # Handle edge cases
    if not s:
        return []
    
    # Dict to store palindromes grouped by length
    palindrome_groups = {}
    
    # Check all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Extract substring
            substring = s[i:j+1]
            
            # Check if substring is a palindrome
            if substring == substring[::-1]:
                # Group palindromes by length
                if len(substring) not in palindrome_groups:
                    palindrome_groups[len(substring)] = set()
                palindrome_groups[len(substring)].add(substring)
    
    # If no palindromes found, return empty list
    if not palindrome_groups:
        return []
    
    # Find the minimum length
    min_length = min(palindrome_groups.keys())
    full_length = max(len(s), 1)
    
    # Collect shortest palindromes and full-length palindrome
    result_set = set()
    
    # Add shortest palindromes
    result_set.update(palindrome_groups[min_length])
    
    # Optionally add unique full-length palindrome if different from shortest
    if full_length > min_length:
        full_palindromes = palindrome_groups.get(full_length, set())
        if len(full_palindromes) == 1:
            result_set.update(full_palindromes)
    
    # Return sorted list
    return sorted(list(result_set))