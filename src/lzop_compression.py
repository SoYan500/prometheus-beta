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
    
    # Compress the data using LZO1X algorithm with maximum compression
    compressed_data = lzo.compress(data, 9)
    
    # Add LZOP header and metadata
    header = b'\x4c\x5a\x4f\x00'  # Magic bytes LZO\0
    version = b'\x11\x00'         # Version 1.1
    method = b'\x02\x00'          # LZO1X-999
    flags = b'\x00\x00\x00\x00'   # No flags
    extra_flags = b'\x00'
    level = b'\x09'               # Compression level 9
    mode = b'\x00\x00\x00\x00'    # Mode
    mtime = b'\x00\x00\x00\x00'   # Modification time
    original_length = struct.pack('>I', len(data))
    compressed_length = struct.pack('>I', len(compressed_data))
    
    # Calculate checksums
    adler32_original = struct.pack('>I', zlib.adler32(data) & 0xffffffff)
    adler32_compressed = struct.pack('>I', zlib.adler32(compressed_data) & 0xffffffff)
    
    # Combine all parts
    compressed_result = (
        header + version + method + flags + extra_flags + level +
        mode + mtime + original_length + compressed_length +
        adler32_original + adler32_compressed + compressed_data
    )
    
    return compressed_result