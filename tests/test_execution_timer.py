import pytest
import time
import logging
from src.execution_timer import log_execution_time

# Capture log messages for testing
class LogCapture:
    def __init__(self):
        self.log_messages = []
    
    def info(self, msg):
        self.log_messages.append(msg)
    
    def error(self, msg):
        self.log_messages.append(msg)

def test_log_execution_time_basic():
    """Test basic functionality of execution time logging"""
    # Create a custom logger
    logger = LogCapture()
    
    # Define a test function with the decorator
    @log_execution_time(logger)
    def test_func():
        time.sleep(0.1)  # Simulate some work
    
    # Call the function
    test_func()
    
    # Check log message
    assert len(logger.log_messages) == 1
    log_msg = logger.log_messages[0]
    assert 'test_func' in log_msg
    assert 'executed in' in log_msg

def test_log_execution_time_with_args():
    """Test execution time logging with function arguments"""
    logger = LogCapture()
    
    @log_execution_time(logger)
    def add_numbers(a, b):
        time.sleep(0.05)
        return a + b
    
    result = add_numbers(3, 4)
    assert result == 7
    
    assert len(logger.log_messages) == 1
    log_msg = logger.log_messages[0]
    assert 'add_numbers' in log_msg
    assert 'executed in' in log_msg

def test_log_execution_time_default_logger():
    """Test execution time logging with default logger"""
    @log_execution_time()
    def quick_func():
        pass
    
    # This should not raise any exceptions
    quick_func()

def test_log_execution_time_exception():
    """Test error logging when an exception occurs"""
    logger = LogCapture()
    
    @log_execution_time(logger)
    def error_func():
        raise ValueError("Test error")
    
    # Expect the original exception to be raised
    with pytest.raises(ValueError, match="Test error"):
        error_func()
    
    # Check that an error was logged
    assert len(logger.log_messages) == 1
    assert 'Error in error_func' in logger.log_messages[0]

def test_log_execution_time_performance():
    """Basic performance test to ensure minimal overhead"""
    logger = LogCapture()
    
    @log_execution_time(logger)
    def fast_func():
        # Very quick operation
        x = 2 + 2
    
    start_time = time.time()
    fast_func()
    total_time = time.time() - start_time
    
    # Logging overhead should be minimal (less than 0.01 seconds)
    assert total_time < 0.01