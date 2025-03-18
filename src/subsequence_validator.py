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
    def can_divide(current_index: int, prev_type: str = None, used: set = None) -> bool:
        # Initialize used set if not provided
        used = used or set()
        
        # Base case: reached the end of the string
        if current_index == len(s):
            return True
        
        # If we've used this index already, we can't use it again
        if current_index in used:
            return False
        
        # Try different subsequence lengths
        found_valid_division = False
        for length in range(2, len(s) - current_index + 1):
            subsequence = s[current_index:current_index + length]
            
            # Check if subsequence is valid
            if not is_valid_subsequence(subsequence):
                continue
            
            # Check current subsequence type
            current_type = 'vowel' if subsequence[0] in vowels else 'consonant'
            
            # Prevent consecutive subsequences of same type
            if prev_type is not None and current_type == prev_type:
                continue
            
            # Mark these indices as used
            new_used = used.copy()
            new_used.update(range(current_index, current_index + length))
            
            # Recursively try to divide the rest of the string
            if can_divide(current_index + length, current_type, new_used):
                found_valid_division = True
                break
        
        return found_valid_division
    
    return can_divide(0)