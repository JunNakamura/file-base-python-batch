from mixin.direcotry.existence_assured_directory import ExistenceAssuredDirectory
from app_name import APP_NAME
from logging import getLogger

from mixin.direcotry.removable_directory import RemovableDirectory

logger = getLogger(APP_NAME).getChild(__name__)


class WorkDirectory(ExistenceAssuredDirectory, RemovableDirectory):

    def __init__(self):
        super().__init__('tmp', 'work')
        logger.debug(f'work directory: {self.path.resolve()}')
