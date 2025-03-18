import lzo

def lzop_compress(data):
    """
    Implement LZO compression for given input data.
    
    Args:
        data (bytes): Input data to be compressed
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input data is empty
    """
    # Validate input
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Compress the data using python-lzo with the fastest compression level
    try:
        # Check if data can potentially be compressed
        if len(data) <= 10:  # For very small data, compression might not reduce size
            return data
        
        compressed_data = lzo.compress(data, 1)
        
        # If compression does not reduce size, return original data
        return compressed_data if len(compressed_data) < len(data) else data
    
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")