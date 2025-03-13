def is_balanced_parentheses(s: str) -> bool:
    """
    Check if a string of parentheses is balanced.

    A string of parentheses is considered balanced if:
    - Every opening parenthesis '(' has a corresponding closing parenthesis ')'
    - Parentheses are closed in the correct order
    - Empty string is considered balanced

    Args:
        s (str): A string containing only parentheses characters

    Returns:
        bool: True if parentheses are balanced, False otherwise

    Raises:
        ValueError: If the input string contains characters other than '(' or ')'
    """
    # Validate input contains only parentheses
    if not all(char in '()' for char in s):
        raise ValueError("Input must contain only parentheses")
    
    # Keep track of open parentheses
    stack = []
    
    for char in s:
        if char == '(':
            # Push opening parenthesis onto stack
            stack.append(char)
        else:  # char == ')'
            # If closing parenthesis with no matching open parenthesis
            if not stack:
                return False
            
            # Remove the last open parenthesis
            stack.pop()
    
    # Balanced if stack is empty
    return len(stack) == 0