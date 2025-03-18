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

    Rules:
    1. Each subsequence must be at least 2 letters long
    2. Subsequences must alternate between vowel and consonant
    3. The entire string must be used
    """
    # Validate input
    if not s or not s.islower() or not s.isalpha():
        return False

    # Define vowels and consonants
    vowels = set('aeiou')
    
    def subsequence_type(subseq: str) -> str:
        """Determine if a subsequence is vowel or consonant."""
        if len(subseq) < 2:
            return None
        
        # All vowels
        if all(char in vowels for char in subseq):
            return 'vowel'
        
        # All consonants
        if all(char not in vowels for char in subseq):
            return 'consonant'
        
        return None
    
    def divide_subsequences(index: int, prev_type: str = None, used_indices: set = None) -> bool:
        """
        Recursive function to divide the string into valid subsequences
        
        Args:
            index: Current starting index
            prev_type: Type of the previous subsequence
            used_indices: Indices already used in subsequences
        
        Returns:
            bool: Whether a valid division exists
        """
        # Initialize used indices
        used_indices = used_indices or set()
        
        # Base case: Successfully used entire string
        if index == len(s):
            # Ensure all indices were used
            return len(used_indices) == len(s)
        
        # Prevent going out of bounds
        if index >= len(s):
            return False
        
        # Try subsequence lengths
        for length in range(2, len(s) - index + 1):
            subsequence = s[index:index+length]
            
            # Get subsequence type
            current_type = subsequence_type(subsequence)
            
            # Skip invalid subsequences
            if current_type is None:
                continue
            
            # Skip if this type is the same as the previous
            if current_type == prev_type:
                continue
            
            # Prevent index reuse
            if any(idx in used_indices for idx in range(index, index+length)):
                continue
            
            # Create new used indices set
            new_used_indices = used_indices.copy()
            new_used_indices.update(range(index, index+length))
            
            # Recursively try to divide the rest of the string
            if divide_subsequences(index + length, current_type, new_used_indices):
                return True
        
        return False
    
    return divide_subsequences(0)