import lzo
import struct
import zlib

def lzop_compress(data):
    """
    Implement LZOP compression for given input data.
    
    Args:
        data (bytes): Input data to be compressed
    
    Returns:
        bytes: Compressed data in LZOP format
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input data is empty
    """
    # Validate input
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Compress the data using python-lzo
    try:
        compressed_data = lzo.compress(data, 1)
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")
    
    return compressed_data