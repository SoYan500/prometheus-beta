def generate_unique_permutations(input_string):
    """
    Generate all possible unique permutations of a given string.

    Args:
        input_string (str): The input string to generate permutations for.

    Returns:
        list: A list of unique permutations of the input string.

    Raises:
        TypeError: If input is not a string.
        ValueError: If input is None or an empty string.
    """
    # Validate input
    if input_string is None:
        raise ValueError("Input cannot be None")
    
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if len(input_string) == 0:
        return []
    
    # Handle single character case
    if len(input_string) == 1:
        return [input_string]
    
    # Convert to list for easier manipulation
    chars = list(input_string)
    
    # Use a set to store unique permutations
    unique_permutations = set()
    
    def backtrack(start):
        """
        Recursive backtracking to generate unique permutations.
        
        Args:
            start (int): Starting index for permutation generation.
        """
        # Base case: if we've reached the end of the string
        if start == len(chars):
            unique_permutations.add(''.join(chars))
            return
        
        # Try swapping current character with each subsequent character
        for i in range(start, len(chars)):
            # Swap characters
            chars[start], chars[i] = chars[i], chars[start]
            
            # Recurse
            backtrack(start + 1)
            
            # Backtrack (undo the swap)
            chars[start], chars[i] = chars[i], chars[start]
    
    # Start the backtracking process
    backtrack(0)
    
    # Convert set to sorted list for consistent output
    return sorted(list(unique_permutations))