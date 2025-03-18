import pytest
import logging
import io
import sys

from src.logger import log_warning

def test_log_warning_valid_message(caplog):
    """Test logging a valid warning message."""
    caplog.set_level(logging.WARNING)
    log_warning("Test warning message")
    
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == "WARNING"
    assert "Test warning message" in caplog.text

def test_log_warning_raises_type_error():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Warning message must be a string"):
        log_warning(123)
    
    with pytest.raises(TypeError, match="Warning message must be a string"):
        log_warning(None)

def test_log_warning_raises_value_error():
    """Test that ValueError is raised for empty string input."""
    with pytest.raises(ValueError, match="Warning message cannot be empty"):
        log_warning("")
    
    with pytest.raises(ValueError, match="Warning message cannot be empty"):
        log_warning("   ")

def test_log_warning_different_messages(caplog):
    """Test logging multiple different warning messages."""
    caplog.set_level(logging.WARNING)
    
    log_warning("First warning")
    log_warning("Second warning")
    
    assert len(caplog.records) == 2
    assert "First warning" in caplog.text
    assert "Second warning" in caplog.text