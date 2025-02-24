"""
Module for logging the length of strings or arrays.
"""
import logging

def log_length(item):
    """
    Log the length of a given string or array.

    Args:
        item (str or list or tuple): The item whose length will be logged.

    Returns:
        int: The length of the input item.

    Raises:
        TypeError: If the input is not a string, list, or tuple.
    """
    # Validate input type
    if not isinstance(item, (str, list, tuple)):
        raise TypeError("Input must be a string, list, or tuple")
    
    # Get the length of the item
    length = len(item)
    
    # Log the length using the logging module
    logging.info(f"Length of {type(item).__name__}: {length}")
    
    return length