import pytest
import socket
from src.dns_lookup import perform_dns_lookup

def test_successful_dns_lookup():
    """Test successful DNS lookup for a known hostname."""
    # Google's hostname
    result = perform_dns_lookup('google.com')
    assert isinstance(result, str)
    # Validate it looks like an IP address
    parts = result.split('.')
    assert len(parts) == 4
    assert all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)

def test_localhost_lookup():
    """Test DNS lookup for localhost."""
    result = perform_dns_lookup('localhost')
    assert result in ['127.0.0.1', '::1']

def test_invalid_input_types():
    """Test handling of invalid input types."""
    with pytest.raises(ValueError, match="Hostname must be a string"):
        perform_dns_lookup(123)
    
    with pytest.raises(ValueError, match="Hostname must be a string"):
        perform_dns_lookup(None)

def test_empty_hostname():
    """Test handling of empty hostname."""
    with pytest.raises(ValueError, match="Hostname cannot be empty"):
        perform_dns_lookup('')
    
    with pytest.raises(ValueError, match="Hostname cannot be empty"):
        perform_dns_lookup('   ')

def test_extremely_long_hostname():
    """Test handling of extremely long hostname."""
    long_hostname = 'a' * 256
    with pytest.raises(ValueError, match="Hostname is too long"):
        perform_dns_lookup(long_hostname)

def test_nonexistent_hostname():
    """Test handling of nonexistent hostname."""
    with pytest.raises(socket.gaierror):
        perform_dns_lookup('thishoesnotexist12345.com')

def test_whitespace_handling():
    """Test that whitespace is stripped from hostname."""
    result = perform_dns_lookup('  google.com  ')
    assert isinstance(result, str)
    parts = result.split('.')
    assert len(parts) == 4
    assert all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)