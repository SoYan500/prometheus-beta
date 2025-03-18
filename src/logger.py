import logging

def log_warning(message):
    """
    Log a warning message to the console.

    Args:
        message (str): The warning message to log.

    Raises:
        TypeError: If the message is not a string.
        ValueError: If the message is an empty string.
    """
    # Validate input
    if not isinstance(message, str):
        raise TypeError("Warning message must be a string")
    
    if not message.strip():
        raise ValueError("Warning message cannot be empty")
    
    # Configure logging to output to console
    logging.basicConfig(
        level=logging.WARNING, 
        format='%(levelname)s: %(message)s'
    )
    
    # Log the warning
    logging.warning(message)