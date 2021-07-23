from mixin.direcotry.existence_assured_directory import ExistenceAssuredDirectory
from app_name import APP_NAME
from logging import getLogger

logger = getLogger(APP_NAME).getChild(__name__)


class OutputDirectory(ExistenceAssuredDirectory):

    def __init__(self):
        super().__init__('nfs', 'output')
        logger.info(f'output directory: {self.path}')

    @property
    def trigger_file(self):
        return self.path.joinpath('end')
