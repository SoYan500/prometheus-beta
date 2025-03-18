import re

def to_snake_case(text: str) -> str:
    """
    Convert a given string to snake_case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The input string converted to snake_case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> to_snake_case("HelloWorld")
        'hello_world'
        >>> to_snake_case("snake_case")
        'snake_case'
        >>> to_snake_case("camelCase")
        'camel_case'
        >>> to_snake_case("PascalCase")
        'pascal_case'
        >>> to_snake_case("mixed Case With Spaces")
        'mixed_case_with_spaces'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Replace non-alphanumeric characters with spaces
    text = re.sub(r'[^a-zA-Z0-9]', ' ', text)
    
    # Insert underscore before any uppercase letter 
    # that is preceded by a lowercase letter or number
    text = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', text)
    
    # Convert to lowercase and replace multiple spaces with single underscore
    return re.sub(r'\s+', '_', text.lower()).strip('_')