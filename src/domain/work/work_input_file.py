from typing import TypeVar, Generic

from domain.input.input_file import InputFile
from domain.work.work_directory import WorkDirectory
import shutil
import gzip
from app_name import APP_NAME
from logging import getLogger

logger = getLogger(APP_NAME).getChild(__name__)

T = TypeVar('T', bound=InputFile)


class WorkInputFile(Generic[T]):

    def __init__(self, input_file: T, work_directory: WorkDirectory):
        """
        copy input file to work directory with gzip compression,
        then delete original file
        """
        self.__path = work_directory.path.joinpath(f'{input_file.name}.gz')
        with open(input_file.path, 'rb') as source_file, gzip.open(self.__path, 'wb') as work_file:
            shutil.copyfileobj(source_file, work_file)
            logger.debug(f'copied {input_file.name} with gzip compression')
            input_file.unlink()
            logger.info(f'moved {input_file.name} to work directory as {self.__path}')

    @property
    def path(self):
        return self.__path

    @property
    def name(self):
        return self.__path.name
