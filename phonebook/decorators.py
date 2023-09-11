from functools import wraps
import logging
import time


def logger(func):
    filename = "user_logs.txt"
    level = logging.INFO
    fmt = "[%(levelname)s] %(asctime)s - %(message)s"
    logging.basicConfig(filename=filename, level=level, format=fmt)

    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"{func.__name__} - {args[1]}")

        return func(*args, **kwargs)

    return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        exec_time = time.perf_counter() - start
        logging.info(f"took {exec_time:.3f} seconds to execute")

        return result

    return wrapper
