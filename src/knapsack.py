def solve_knapsack(weights, values, capacity):
    """
    Solve the 0/1 Knapsack problem using dynamic programming.
    
    Args:
        weights (list): List of item weights
        values (list): List of item values 
        capacity (int): Maximum weight capacity of the knapsack
    
    Returns:
        tuple: A tuple containing:
            - Maximum total value that can be achieved
            - List of items selected (indices)
    
    Raises:
        ValueError: If input lists have different lengths or negative capacity
    """
    # Input validation
    if len(weights) != len(values):
        raise ValueError("Weights and values lists must have the same length")
    if capacity < 0:
        raise ValueError("Knapsack capacity must be non-negative")
    
    # Number of items
    n = len(weights)
    
    # Initialize dynamic programming table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build the table bottom-up
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't include current item
            dp[i][w] = dp[i-1][w]
            
            # Try to include current item if possible
            if weights[i-1] <= w:
                dp[i][w] = max(
                    dp[i][w], 
                    dp[i-1][w - weights[i-1]] + values[i-1]
                )
    
    # Track selected items (backtracking)
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
    
    selected_items.reverse()
    
    return dp[n][capacity], selected_items