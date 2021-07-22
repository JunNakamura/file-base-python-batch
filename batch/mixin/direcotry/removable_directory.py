from abc import ABC, abstractmethod
from pathlib import Path
import shutil


class RemovableDirectory(ABC):

    @property
    @abstractmethod
    def path(self) -> Path:
        raise NotImplementedError

    def remove_if_exists(self):
        if self.path.exists():
            shutil.rmtree(self.path)
