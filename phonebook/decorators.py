from functools import wraps
import logging


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
