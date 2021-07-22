from abc import ABC, abstractmethod
from pathlib import Path
import shutil
from app_name import APP_NAME
from logging import getLogger

logger = getLogger(APP_NAME).getChild(__name__)


class RemovableDirectory(ABC):

    @property
    @abstractmethod
    def path(self) -> Path:
        raise NotImplementedError

    def remove_if_exists(self):
        if self.path.exists():
            shutil.rmtree(self.path)
            logger.info(f'removed {self.path}')
