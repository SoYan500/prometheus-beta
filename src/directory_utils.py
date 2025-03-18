import os
from typing import Union, Optional, AnyStr

def directory_exists(path: Union[str, bytes, os.PathLike]) -> bool:
    """
    Check if a directory exists at the specified path.

    Args:
        path (Union[str, bytes, os.PathLike]): The path to the directory to check.

    Returns:
        bool: True if the path exists and is a directory, False otherwise.

    Raises:
        TypeError: If the input path is None.
    """
    if path is None:
        raise TypeError("Path cannot be None")
    
    try:
        return os.path.isdir(path)
    except TypeError:
        return False