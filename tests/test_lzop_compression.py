import pytest
import lzo
import zlib
import struct

from src.lzop_compression import lzop_compress

def test_lzop_compress_basic():
    """Test basic compression of a simple string"""
    input_data = b"Hello, world! This is a test of LZOP compression."
    compressed = lzop_compress(input_data)
    
    # Validate basic structure
    assert len(compressed) > 0
    assert len(compressed) < len(input_data)

def test_lzop_compress_header():
    """Test the header structure of the compressed data"""
    input_data = b"Test compression header"
    compressed = lzop_compress(input_data)
    
    # Check version (should be 0x1010)
    version = struct.unpack('>H', compressed[0:2])[0]
    assert version == 0x1010
    
    # Check method (should be 0x0020 for LZO1X)
    method = struct.unpack('>H', compressed[2:4])[0]
    assert method == 0x0020

def test_lzop_compress_error_handling():
    """Test error handling for invalid inputs"""
    # Test with non-bytes input
    with pytest.raises(TypeError):
        lzop_compress("Not bytes")
    
    # Test with empty input
    with pytest.raises(ValueError):
        lzop_compress(b"")

def test_lzop_compress_decompression():
    """Verify that compressed data can be decompressed"""
    input_data = b"Compression and decompression test with LZO"
    compressed = lzop_compress(input_data)
    
    # Extract compressed data (skip header and checksum)
    header_size = 16  # 2+2+1+1+4+4+4 bytes
    checksum_size = 4
    compressed_payload = compressed[header_size+checksum_size:]
    
    # Decompress and verify
    decompressed = lzo.decompress(compressed_payload)
    assert decompressed == input_data

def test_lzop_compress_large_data():
    """Test compression of larger data"""
    input_data = b"A" * 10000  # Large repetitive data
    compressed = lzop_compress(input_data)
    
    assert len(compressed) > 0
    assert len(compressed) < len(input_data)