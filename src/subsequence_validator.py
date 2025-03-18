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
    
    # Recursive function to explore all possible divisions
    def divide_subsequences(index: int, last_subsequence_type: str = None, used_indices: set = None) -> bool:
        # Initialize used_indices if not provided
        used_indices = used_indices or set()
        
        # Successfully reached the end of the string
        if index == len(s):
            return True
        
        # Prevent using already used indices
        if index in used_indices:
            return False
        
        # Try subsequences of different lengths
        for length in range(2, len(s) - index + 1):
            # Extract potential subsequence
            subsequence = s[index:index+length]
            
            # Skip invalid subsequences
            if not is_valid_subsequence(subsequence):
                continue
            
            # Determine subsequence type (vowel or consonant)
            current_type = 'vowel' if subsequence[0] in vowels else 'consonant'
            
            # Prevent consecutive same-type subsequences
            if current_type == last_subsequence_type:
                continue
            
            # Create a new set of used indices
            new_used_indices = used_indices.copy()
            new_used_indices.update(range(index, index + length))
            
            # Recursively try to divide the rest of the string
            if divide_subsequences(index + length, current_type, new_used_indices):
                return True
        
        # No valid division found
        return False
    
    return divide_subsequences(0)