import os
import logging
import pytest
import tempfile
from src.menu_logger import MenuLogger

def test_menu_logger_initialization():
    """Test basic initialization of MenuLogger"""
    logger = MenuLogger()
    assert isinstance(logger, MenuLogger)
    assert logger.logger.level == logging.INFO

def test_menu_logger_with_custom_log_file():
    """Test MenuLogger with a custom log file"""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_log:
        temp_log_path = temp_log.name
    
    logger = MenuLogger(log_file=temp_log_path)
    logger.log_selection('test_menu', 'option1', 'user123')
    
    # Read the log file contents
    with open(temp_log_path, 'r') as f:
        log_contents = f.read()
    
    # Clean up
    os.unlink(temp_log_path)
    
    # Assert log contains expected information
    assert 'Menu: test_menu' in log_contents
    assert 'Selection: option1' in log_contents
    assert 'User: user123' in log_contents

def test_log_selection_without_user_id():
    """Test logging a selection without a user ID"""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_log:
        temp_log_path = temp_log.name
    
    logger = MenuLogger(log_file=temp_log_path)
    logger.log_selection('main_menu', 'exit')
    
    # Read the log file contents
    with open(temp_log_path, 'r') as f:
        log_contents = f.read()
    
    # Clean up
    os.unlink(temp_log_path)
    
    # Assert log contains expected information
    assert 'Menu: main_menu' in log_contents
    assert 'Selection: exit' in log_contents

def test_log_selection_empty_menu_name():
    """Test that logging with an empty menu name raises a ValueError"""
    logger = MenuLogger()
    
    with pytest.raises(ValueError, match="Menu name cannot be empty"):
        logger.log_selection('', 'some_option')

def test_get_log_entries():
    """Test retrieving log entries"""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_log:
        # Write some sample log entries
        temp_log.write("2023-01-01 10:00:00 - INFO - Menu: menu1, Selection: option1\n")
        temp_log.write("2023-01-01 11:00:00 - INFO - Menu: menu2, Selection: option2\n")
        temp_log.flush()
        temp_log_path = temp_log.name
    
    logger = MenuLogger()
    entries = logger.get_log_entries(log_file=temp_log_path)
    
    # Clean up
    os.unlink(temp_log_path)
    
    # Assert retrieved entries
    assert len(entries) == 2
    assert 'Menu: menu1, Selection: option1' in entries[0]
    assert 'Menu: menu2, Selection: option2' in entries[1]

def test_get_log_entries_max_limit():
    """Test retrieving log entries with a maximum limit"""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_log:
        # Write multiple log entries
        for i in range(1, 6):
            temp_log.write(f"2023-01-01 {i}:00:00 - INFO - Menu: menu{i}, Selection: option{i}\n")
        temp_log.flush()
        temp_log_path = temp_log.name
    
    logger = MenuLogger()
    entries = logger.get_log_entries(log_file=temp_log_path, max_entries=2)
    
    # Clean up
    os.unlink(temp_log_path)
    
    # Assert retrieved entries are the last 2
    assert len(entries) == 2
    assert 'Menu: menu4, Selection: option4' in entries[0]
    assert 'Menu: menu5, Selection: option5' in entries[1]

def test_get_log_entries_nonexistent_file():
    """Test retrieving log entries from a nonexistent file"""
    logger = MenuLogger()
    entries = logger.get_log_entries(log_file='/path/to/nonexistent/file.log')
    
    # Assert empty list is returned
    assert entries == []