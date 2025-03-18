import time
from functools import wraps
from typing import Callable, Any


def measure_execution_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator that measures and prints the execution time of a function.

    Args:
        func (Callable): The function whose execution time is to be measured.

    Returns:
        Callable: A wrapped function that prints execution time before returning result.

    Example:
        @measure_execution_time
        def example_function(n):
            return sum(range(n))
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Record start time
        start_time = time.perf_counter()

        try:
            # Execute the function
            result = func(*args, **kwargs)
        except Exception as e:
            # If an exception occurs, re-raise it after timing
            raise e
        finally:
            # Calculate and print execution time
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            print(f"Function '{func.__name__}' took {execution_time:.6f} seconds to execute")

        return result

    return wrapper


def get_execution_time(func: Callable[..., Any], *args: Any, **kwargs: Any) -> tuple[Any, float]:
    """
    Measure the execution time of a function and return both the result and the time taken.

    Args:
        func (Callable): The function to measure.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.

    Returns:
        tuple: A tuple containing the function's result and its execution time in seconds.

    Example:
        result, time_taken = get_execution_time(sum, range(1000000))
    """
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    
    execution_time = end_time - start_time
    return result, execution_time