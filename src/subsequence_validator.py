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
    3. No index can be used more than once
    4. The entire string must be used
    """
    # Validate input
    if not s or not s.islower() or not s.isalpha():
        return False

    # Define vowels and consonants
    vowels = set('aeiou')
    
    def is_vowel_subsequence(subseq: str) -> bool:
        return len(subseq) >= 2 and all(char in vowels for char in subseq)
    
    def is_consonant_subsequence(subseq: str) -> bool:
        return len(subseq) >= 2 and all(char not in vowels for char in subseq)
    
    def divide_subsequences(index: int, used_indices: set, prev_type: str = None) -> bool:
        # Base case: Successfully used entire string
        if index == len(s):
            return True
        
        # If current index already used, fail
        if index in used_indices:
            return False
        
        # Try subsequence lengths
        for length in range(2, len(s) - index + 1):
            subsequence = s[index:index+length]
            
            # Determine subsequence type
            current_type = 'vowel' if subsequence[0] in vowels else 'consonant'
            
            # Skip if this type is the same as the previous
            if current_type == prev_type:
                continue
            
            # Check subsequence validity based on type
            if current_type == 'vowel' and not is_vowel_subsequence(subsequence):
                continue
            if current_type == 'consonant' and not is_consonant_subsequence(subsequence):
                continue
            
            # Create new set of used indices
            new_used_indices = used_indices.copy()
            new_used_indices.update(range(index, index+length))
            
            # Recursively try to divide the rest of the string
            if divide_subsequences(index + length, new_used_indices, current_type):
                return True
        
        return False
    
    return divide_subsequences(0, set())