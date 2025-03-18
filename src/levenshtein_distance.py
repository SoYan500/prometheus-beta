def levenshtein_distance(str1, str2):
    """
    Compute the Levenshtein distance between two strings using dynamic programming.
    
    The Levenshtein distance is the minimum number of single-character edits 
    (insertions, deletions, or substitutions) required to transform one string into another.
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        int: The Levenshtein distance between str1 and str2
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Validate input types
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Inputs must be strings")
    
    # Create a matrix to store distances
    m, n = len(str1), len(str2)
    
    # Initialize the distance matrix
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill first row and column with incremental costs
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Compute the Levenshtein distance
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters are the same, no edit cost
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Minimum of insert, delete, or substitute
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # deletion
                    dp[i][j-1],    # insertion
                    dp[i-1][j-1]   # substitution
                )
    
    # Return the final distance
    return dp[m][n]