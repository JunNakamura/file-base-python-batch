import shutil

from domain.backup.backup_directory import BackupDirectory
from mixin.direcotry.existence_assured_directory import ExistenceAssuredDirectory
from app_name import APP_NAME
from logging import getLogger

from mixin.direcotry.removable_directory import RemovableDirectory

logger = getLogger(APP_NAME).getChild(__name__)


class WorkDirectory(ExistenceAssuredDirectory, RemovableDirectory):

    def __init__(self):
        super().__init__('tmp', 'work')
        logger.info(f'work directory: {self.path}')

    def move_files_to(self, backup_directory: BackupDirectory):
        target_files = [path for path in self.path.iterdir() if path.is_file()]
        for file in target_files:
            shutil.move(file, backup_directory.path.joinpath(file.name))
        logger.info(f'moved {target_files} to backup directory')
