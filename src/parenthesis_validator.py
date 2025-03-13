def is_nested_parentheses(s: str) -> bool:
    """
    Determine if parentheses in a string are correctly nested.
    
    Args:
        s (str): Input string containing parentheses to validate
    
    Returns:
        bool: True if parentheses are correctly nested, False otherwise
    
    Examples:
        >>> is_nested_parentheses("()")  # Simple nested
        True
        >>> is_nested_parentheses("(())")  # Complex nested
        True
        >>> is_nested_parentheses(")(")  # Incorrect order
        False
        >>> is_nested_parentheses("(()")  # Unbalanced
        False
    """
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            # If closing parenthesis when stack is empty, it's not nested
            if not stack:
                return False
            stack.pop()
    
    # Stack should be empty for perfect nesting
    return len(stack) == 0