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
        # Use LZO1X compression
        compressed_data = lzo.compress(data, compression_level)
        
        # Prepend compressed data with original size to help decompression
        original_size = struct.pack('>I', len(data))
        
        # Fully compressed payload
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
    
    try:
        # Extract original size
        original_size = struct.unpack('>I', compressed_data[:4])[0]
        
        # Decompress remaining data
        decompressed_data = lzo.decompress(compressed_data[4:])
        
        # Verify decompressed data size
        if len(decompressed_data) != original_size:
            raise ValueError("Decompression size mismatch")
        
        return decompressed_data
    
    except Exception as e:
        raise RuntimeError(f"Decompression failed: {str(e)}")