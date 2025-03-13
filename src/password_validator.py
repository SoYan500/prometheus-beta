import re

def validate_password(password):
    """
    Validate a password based on the following complexity requirements:
    - Minimum length of 8 characters
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character (!, @, #, $, %, ^, &, *)
    - No whitespace characters allowed

    Args:
        password (str): The password to validate

    Returns:
        bool: True if the password meets all complexity requirements, False otherwise
    
    Raises:
        TypeError: If the input is not a string
    """
    # Check if input is a string
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    
    # Check for whitespace
    if re.search(r'\s', password):
        return False
    
    # Check minimum length
    if len(password) < 8:
        return False
    
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    
    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    
    # Check for at least one digit
    if not re.search(r'\d', password):
        return False
    
    # Check for at least one special character
    if not re.search(r'[!@#$%^&*]', password):
        return False
    
    # If all checks pass, return True
    return True