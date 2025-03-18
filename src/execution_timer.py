import time
import functools
import logging
from typing import Callable, Any

def log_execution_time(logger: logging.Logger = None) -> Callable:
    """
    A decorator to log the execution time of a function.

    Args:
        logger (logging.Logger, optional): Logger to use for recording execution time. 
                Defaults to None, which uses the root logger.

    Returns:
        Callable: Decorated function that logs its execution time.

    Example:
        >>> import logging
        >>> logging.basicConfig(level=logging.INFO)
        >>> @log_execution_time()
        ... def example_function(x, y):
        ...     time.sleep(0.1)
        ...     return x + y
        >>> result = example_function(1, 2)
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Use provided logger or get root logger
            log = logger or logging.getLogger()
            
            # Start timing
            start_time = time.time()
            
            try:
                # Execute the function
                result = func(*args, **kwargs)
            except Exception as e:
                # Log any exceptions that occur
                log.error(f"Error in {func.__name__}: {e}")
                raise
            finally:
                # Calculate and log execution time
                end_time = time.time()
                execution_time = end_time - start_time
                log.info(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
            
            return result
        return wrapper
    return decorator