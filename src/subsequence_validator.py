def can_divide_subsequences(s: str) -> bool:
    """
    Determine if a string of lowercase English letters can be divided into 
    subsequences of at least 2 letters, where each subsequence is either 
    all vowels or all consonants.

    Args:
        s (str): A string of lowercase English letters.

    Returns:
        bool: True if the string can be divided into valid subsequences, 
              False otherwise.

    Raises:
        ValueError: If the input string contains non-lowercase English letters.
    """
    # Validate input
    if not s or not s.islower() or not s.isalpha():
        return False

    # Define vowels and consonants
    vowels = set('aeiou')
    
    # Helper function to check if a subsequence is valid
    def is_valid_subsequence(subseq: str) -> bool:
        # Check if subsequence is at least 2 characters long
        if len(subseq) < 2:
            return False
        
        # Check if all characters are either vowels or consonants
        return all(char in vowels for char in subseq) or \
               all(char not in vowels for char in subseq)
    
    # Try all possible divisions of the string
    def can_divide(current_index: int) -> bool:
        # Base case: reached the end of the string
        if current_index == len(s):
            return True
        
        # Try different subsequence lengths starting from current index
        for length in range(2, len(s) - current_index + 1):
            subsequence = s[current_index:current_index + length]
            
            # If this subsequence is valid, try dividing the rest of the string
            if is_valid_subsequence(subsequence):
                if can_divide(current_index + length):
                    return True
        
        return False
    
    return can_divide(0)