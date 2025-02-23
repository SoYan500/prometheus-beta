import os

def file_exists(file_path):
    """
    Determine if a file exists at the given path.

    Args:
        file_path (str): The relative or absolute path to the file.

    Returns:
        bool: True if the file exists and is a regular file, False otherwise.

    Raises:
        TypeError: If the file_path is not a string.
    """
    # Check if input is a string
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")

    # Normalize the path and check if it exists and is a file
    return os.path.isfile(os.path.expanduser(file_path))