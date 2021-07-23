from pathlib import Path
import yaml
from logging import config, getLogger
from app_name import APP_NAME
from backup.backup_directory import BackupDirectory
from decorator.logging import timed
from file_base_batch import FileBaseBatch
from file_lock import PIDFileLock
from input.entry_file import EntryFile
from input.input_directory import InputDirectory
from input.order_history_file import OrderHistoryFile
from output.output_directory import OutputDirectory
from output.result_file import ResultFile
from work.work_directory import WorkDirectory
from work.work_entry_file import WorkEntryFile
from work.work_order_history_file import WorkOrderHistoryFile

logger = getLogger(APP_NAME).getChild(__name__)


def main():
    batch = FileBaseBatch()
    batch.start()


if __name__ == '__main__':
    Path('logs').mkdir(exist_ok=True)
    logging_config_file = Path('logging.yaml')
    with logging_config_file.open() as f:
        log_dict_config = yaml.safe_load(f)
        config.dictConfig(log_dict_config)
    main()
