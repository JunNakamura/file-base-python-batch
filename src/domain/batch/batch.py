from abc import ABC, abstractmethod
from app_name import APP_NAME
from logging import getLogger

from domain.batch.file_lock import PIDFileLock

logger = getLogger(APP_NAME).getChild(__name__)


class BatchWithFileLock(ABC):

    def __init__(self, batch_name: str):
        self.__name = batch_name

    @property
    def name(self):
        return self.__name

    def start(self):
        lock = PIDFileLock(self.name)
        if lock.is_locked:
            logger.info(f'stop this process of {self.name} since another process({lock.pid()}) is in progress.')
            return
        with lock:
            self.execute()

    @abstractmethod
    def execute(self):
        raise NotImplementedError
