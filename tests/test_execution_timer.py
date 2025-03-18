import time
import pytest
from src.execution_timer import measure_execution_time, get_execution_time


def test_measure_execution_time_decorator(capsys):
    @measure_execution_time
    def slow_function(n):
        time.sleep(n)
        return n

    result = slow_function(0.1)
    captured = capsys.readouterr()

    assert result == 0.1
    assert "Function 'slow_function' took" in captured.out
    assert "seconds to execute" in captured.out


def test_get_execution_time():
    def test_func(a, b):
        time.sleep(0.1)
        return a + b

    result, execution_time = get_execution_time(test_func, 3, 4)

    assert result == 7
    assert 0.09 < execution_time < 0.11  # Allow some variance


def test_execution_time_with_function_arguments():
    @measure_execution_time
    def multiply(a, b):
        time.sleep(0.05)
        return a * b

    result = multiply(5, 6)
    assert result == 30


def test_execution_time_with_error_handling():
    @measure_execution_time
    def error_function():
        raise ValueError("Test error")

    with pytest.raises(ValueError, match="Test error"):
        error_function()


def test_get_execution_time_error_handling():
    def error_func():
        raise RuntimeError("Another test error")

    with pytest.raises(RuntimeError, match="Another test error"):
        get_execution_time(error_func)