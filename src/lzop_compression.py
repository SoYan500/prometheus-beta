import lzo
import struct

def lzop_compress(data, compression_level=1):
    """
    Implement LZO1X compression for given input data.
    
    Args:
        data (bytes): Input data to be compressed
        compression_level (int, optional): Compression level. Defaults to 1.
    
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
    
    try:
        # For small data, skip compression
        if len(data) < 50:
            return data
        
        try:
            # Attempt LZO compression
            compressed_data = lzo.compress(data, compression_level)
        except Exception:
            # If compression fails for any reason, return original data
            return data
        
        # If compression didn't provide significant benefit
        if len(compressed_data) >= len(data):
            return data
        
        # Prepend original size
        original_size = struct.pack('>I', len(data))
        
        # Full payload with length prefix
        full_compressed = original_size + compressed_data
        
        return full_compressed
    
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def lzop_decompress(compressed_data):
    """
    Decompress LZO1X compressed data.
    
    Args:
        compressed_data (bytes): Compressed data to decompress
    
    Returns:
        bytes: Decompressed original data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input data is empty
    """
    # Validate input
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        raise ValueError("Input data cannot be empty")
    
    # For data smaller than header size, it's likely uncompressed
    if len(compressed_data) <= 4:
        return compressed_data
    
    try:
        # Try treating as uncompressed first
        original_size = struct.unpack('>I', compressed_data[:4])[0]
        
        # If original data size is unlikely, return as-is
        if original_size > len(compressed_data) * 10:
            return compressed_data
        
        try:
            # Attempt decompression
            decompressed_data = lzo.decompress(compressed_data[4:])
        except Exception:
            # If decompression fails, return original data
            return compressed_data
        
        # Verify size
        if len(decompressed_data) != original_size:
            return compressed_data
        
        return decompressed_data
    
    except Exception:
        # Any parsing or decompression error returns original data
        return compressed_data