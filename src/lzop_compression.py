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
    
    # LZOP uses LZO compression with some additional headers
    try:
        # Compress the data using LZO1X algorithm
        compressed_data = lzo.compress(data, 1)
        
        # Create LZOP header
        # Version (2 bytes), method (1 byte), compression level (1 byte)
        # Flags (4 bytes), mode (4 bytes), mtime (4 bytes)
        # Original file size (4 bytes)
        header = struct.pack('>HHBBIHII', 
            0x1010,   # Version 
            0x0020,   # Method (LZO1X)
            1,        # Compression level
            0,        # Reserved 
            0,        # Flags
            0,        # Mode 
            0,        # Modification time
            len(data) # Original file size
        )
        
        # Checksum of original data
        adler32_checksum = zlib.adler32(data) & 0xffffffff
        
        # Combine header, checksum, and compressed data
        compressed_result = header + struct.pack('>I', adler32_checksum) + compressed_data
        
        return compressed_result
    
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")