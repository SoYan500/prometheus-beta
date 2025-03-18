import pytest
import lzo

from src.lzop_compression import lzop_compress

def test_lzop_compress_basic():
    """Test basic compression of a simple string"""
    input_data = b"Hello, world! This is a test of LZOP compression."
    compressed = lzop_compress(input_data)
    
    # Validate basic structure
    assert len(compressed) > 0
    assert len(compressed) < len(input_data)

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
    
    # Decompress and verify
    decompressed = lzo.decompress(compressed)
    assert decompressed == input_data

def test_lzop_compress_large_data():
    """Test compression of larger data"""
    input_data = b"A" * 10000  # Large repetitive data
    compressed = lzop_compress(input_data)
    
    assert len(compressed) > 0
    assert len(compressed) < len(input_data)

def test_lzop_compress_random_data():
    """Test compression of random-like data"""
    import os
    input_data = os.urandom(1000)
    compressed = lzop_compress(input_data)
    
    assert len(compressed) > 0
    decompressed = lzo.decompress(compressed)
    assert decompressed == input_data