from pathlib import Path
import yaml
from logging import config, getLogger
from app_name import APP_NAME
from backup.backup_directory import BackupDirectory
from decorator.logging import timed
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


@timed
def main():
    lock = PIDFileLock('file_base_batch')
    if lock.is_locked:
        logger.info(f'stop this process since another process({lock.pid()}) is in progress.')
        return
    with lock:
        input_directory = InputDirectory()
        if not input_directory.trigger_file.exists():
            logger.info(f'trigger file({input_directory.trigger_file}) does not exist. nothing to do.')
            return
        input_directory.trigger_file.unlink()
        logger.info('start process since trigger file exists')
        order_history_file = OrderHistoryFile(input_directory)
        entry_file = EntryFile(input_directory)
        input_files = [order_history_file, entry_file]
        for input_file in input_files:
            logger.info(f'checksum of {input_file.name}: {input_file.md5_checksum()}')

        work_directory = WorkDirectory()
        work_order_history_file = WorkOrderHistoryFile(order_history_file, work_directory)
        work_entry_file = WorkEntryFile(entry_file, work_directory)

        output_directory = OutputDirectory()
        output_directory.trigger_file.unlink(missing_ok=True)

        result_file = ResultFile(output_directory, work_directory)
        result_file.create(work_order_history_file, work_entry_file)
        output_directory.trigger_file.touch()

        backup_directory = BackupDirectory()
        work_directory.move_files_to(backup_directory)
        work_directory.remove_if_exists()


if __name__ == '__main__':
    Path('logs').mkdir(exist_ok=True)
    logging_config_file = Path('logging.yaml')
    with logging_config_file.open() as f:
        log_dict_config = yaml.safe_load(f)
        config.dictConfig(log_dict_config)
    main()
