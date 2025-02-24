"""
Test module for length_logger function.
"""
import logging
import pytest
from src.length_logger import log_length

def test_log_length_string(caplog):
    """Test logging length of a string."""
    caplog.set_level(logging.INFO)
    
    result = log_length("hello")
    assert result == 5
    
    assert len(caplog.records) == 1
    log_record = caplog.records[0]
    assert log_record.levelno == logging.INFO
    assert "Length of str: 5" in log_record.message

def test_log_length_list(caplog):
    """Test logging length of a list."""
    caplog.set_level(logging.INFO)
    
    test_list = [1, 2, 3, 4]
    result = log_length(test_list)
    assert result == 4
    
    assert len(caplog.records) == 1
    log_record = caplog.records[0]
    assert log_record.levelno == logging.INFO
    assert "Length of list: 4" in log_record.message

def test_log_length_tuple(caplog):
    """Test logging length of a tuple."""
    caplog.set_level(logging.INFO)
    
    test_tuple = (1, 2, 3)
    result = log_length(test_tuple)
    assert result == 3
    
    assert len(caplog.records) == 1
    log_record = caplog.records[0]
    assert log_record.levelno == logging.INFO
    assert "Length of tuple: 3" in log_record.message

def test_log_length_invalid_type():
    """Test that TypeError is raised for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a string, list, or tuple"):
        log_length(123)
    
    with pytest.raises(TypeError, match="Input must be a string, list, or tuple"):
        log_length(None)
    
    with pytest.raises(TypeError, match="Input must be a string, list, or tuple"):
        log_length({})

def test_log_length_empty_items(caplog):
    """Test logging length of empty strings, lists, and tuples."""
    caplog.set_level(logging.INFO)
    
    # Empty string
    result = log_length("")
    assert result == 0
    assert "Length of str: 0" in caplog.records[0].message
    
    # Empty list
    caplog.clear()
    result = log_length([])
    assert result == 0
    assert "Length of list: 0" in caplog.records[0].message
    
    # Empty tuple
    caplog.clear()
    result = log_length(())
    assert result == 0
    assert "Length of tuple: 0" in caplog.records[0].message