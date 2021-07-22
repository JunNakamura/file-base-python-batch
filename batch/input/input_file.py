import hashlib

from input.input_directory import InputDirectory
from app_name import APP_NAME
from logging import getLogger


logger = getLogger(APP_NAME).getChild(__name__)


class InputFile:

    def __init__(self, input_directory: InputDirectory):
        self.__path = input_directory.path.joinpath('input.csv')
        logger.debug(f'input file: {self.__path}')
        assert self.__path.exists()

    @property
    def path(self):
        return self.__path

    @property
    def name(self):
        return self.__path.name

    def unlink(self):
        self.__path.unlink()
        logger.debug(f'removed {self.__path}')

    def md5_checksum(self):
        md5 = hashlib.md5()
        with open(self.path, 'rb') as f:
            for chunk in f:
                md5.update(chunk)
        return md5.hexdigest()




