from abc import ABC
from pathlib import Path


class ExistenceAssuredDirectory(ABC):

    def __init__(self, *segments: str):
        self.__path = Path(*segments)
        self.__path.mkdir(exist_ok=True, parents=True)
        assert self.__path.exists()
        assert self.__path.is_dir()

    @property
    def path(self):
        return self.__path