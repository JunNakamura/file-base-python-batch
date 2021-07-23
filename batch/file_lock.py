import os
from pathlib import Path
from app_name import APP_NAME
from logging import getLogger

logger = getLogger(APP_NAME).getChild(__name__)


class PIDFileLock:
    """
    This lock watches only existence of lock file.
    It could occur dead lock if application crashes.
    In this case, delete lock file simply.
    """

    def __init__(self, name: str):
        self.__lock_file = Path(f'{name}.lock')

    @property
    def lock_file(self):
        return self.__lock_file

    @property
    def is_locked(self):
        return self.lock_file.exists()

    def acquire(self):
        with open(self.lock_file, 'x') as file:
            file.write(str(os.getpid()))
        logger.info(f'acquired {self.lock_file}')

    def pid(self):
        assert self.is_locked
        with open(self.lock_file) as file:
            return int(file.read())

    def release(self):
        assert os.getpid() == self.pid()
        self.lock_file.unlink()
        logger.info(f'released {self.lock_file}')

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()
