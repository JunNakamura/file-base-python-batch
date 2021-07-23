from mixin.direcotry.existence_assured_directory import ExistenceAssuredDirectory


class BackupDirectory(ExistenceAssuredDirectory):

    def __init__(self):
        super().__init__('tmp', 'backup')
