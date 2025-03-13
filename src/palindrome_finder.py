def find_palindrome_substrings(s: str) -> list[str]:
    """
    Find all palindromic substrings in a given string.
    
    A palindromic substring is a sequence of characters that reads 
    the same forwards and backwards.
    
    Args:
        s (str): The input string to search for palindromic substrings.
    
    Returns:
        list[str]: A list of all unique palindromic substrings found in the input string.
    
    Examples:
        >>> find_palindrome_substrings("abba")
        ['a', 'b', 'bb', 'abba']
        >>> find_palindrome_substrings("hello")
        ['h', 'e', 'l', 'l', 'o']
    """
    # Handle edge cases
    if not s:
        return []
    
    # Set to store unique palindromic substrings
    palindromes = set()
    
    # Helper function to expand around center
    def expand_around_center(left: int, right: int) -> None:
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            # Add the palindrome substring to the set
            palindromes.add(s[left:right+1])
            # Expand outwards
            left -= 1
            right += 1
    
    # Check palindromes for each possible center
    for i in range(len(s)):
        # Odd length palindromes (single character center)
        expand_around_center(i, i)
        
        # Even length palindromes (two-character center)
        expand_around_center(i, i+1)
    
    # Convert set to sorted list for consistent output
    return sorted(list(palindromes), key=len)