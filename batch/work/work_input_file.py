from input.input_file import InputFile
from work.work_directory import WorkDirectory
import shutil
import gzip
from app_name import APP_NAME
from logging import getLogger

logger = getLogger(APP_NAME).getChild(__name__)


class WorkInputFile:

    def __init__(self, input_file: InputFile, work_directory: WorkDirectory):
        """
        copy input file to work directory with gzip compression,
        then delete original file
        """
        self.__path = work_directory.path.joinpath(f'{input_file.name}.gz')
        with open(input_file.path, 'rb') as source_file, gzip.open(self.__path, 'wb') as work_file:
            shutil.copyfileobj(source_file, work_file)
            input_file.unlink()
            logger.info(f'moved input file to work directory as {self.__path.name}')
            logger.debug(f'work input file: {self.__path}')

    @property
    def path(self):
        return self.__path

    @property
    def name(self):
        return self.__path.name
