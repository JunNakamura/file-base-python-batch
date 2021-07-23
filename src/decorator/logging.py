from functools import wraps
from datetime import datetime
from app_name import APP_NAME
from logging import getLogger

logger = getLogger(APP_NAME).getChild(__name__)


def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        logger.info(f'[start][{func.__qualname__}]')
        result = func(*args, **kwargs)
        elapsed_time = datetime.now() - start_time
        logger.info(f'[end][{func.__qualname__}] elapsed time: {elapsed_time}')
        return result
    return wrapper
