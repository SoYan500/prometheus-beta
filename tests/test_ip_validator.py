import pytest
from src.ip_validator import validate_ip_address

def test_valid_ip_addresses():
    """Test valid IP address formats"""
    valid_ips = [
        "1.2.3.4",
        "0.0.0.0",
        "9.9.9.9"
    ]
    for ip in valid_ips:
        assert validate_ip_address(ip) is True, f"{ip} should be valid"

def test_invalid_ip_addresses():
    """Test invalid IP address formats"""
    invalid_ips = [
        # Wrong number of octets
        "1.2.3",
        "1.2.3.4.5",
        
        # Non-numeric characters
        "a.b.c.d",
        "1.2.3.x",
        
        # Multi-digit octets
        "10.20.30.40",
        "1.02.3.4",
        
        # Outside single-digit range
        "-1.2.3.4",
        "1.2.3.-4",
        
        # Empty strings and non-string inputs
        "",
        None,
        123,
        [],
        
        # Wrong separators
        "1,2,3,4",
        "1 2 3 4"
    ]
    for ip in invalid_ips:
        assert validate_ip_address(ip) is False, f"{ip} should be invalid"

def test_edge_cases():
    """Test edge case scenarios"""
    # Test single-digit boundaries
    assert validate_ip_address("0.0.0.0") is True
    assert validate_ip_address("9.9.9.9") is True
    
    # Validate type checks
    assert validate_ip_address(None) is False
    assert validate_ip_address(123) is False
    assert validate_ip_address([]) is False