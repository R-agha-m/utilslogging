from functools import wraps
import stg


def logger_decorator(logger=None):
    logger = logger or stg.report

    def inner_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f"entering '{func.__name__}' function", extra={'func_name_override': func.__name__})
            results = func(*args, **kwargs)
            logger.info(f"successfully exiting '{func.__name__}' function", extra={'func_name_override': func.__name__})
            return results
        return wrapper
    return inner_decorator
