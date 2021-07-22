from pathlib import Path
import yaml
from logging import config, getLogger
from app_name import APP_NAME
from backup.backup_directory import BackupDirectory
from input.input_directory import InputDirectory
from input.input_file import InputFile
from output.output_directory import OutputDirectory
from output.result_file import ResultFile
from work.work_directory import WorkDirectory
from work.work_input_file import WorkInputFile

logger = getLogger(APP_NAME).getChild(__name__)


def main():
    logger.info('check trigger file')
    input_directory = InputDirectory()
    if not input_directory.trigger_file.exists():
        logger.info(f'trigger file({input_directory.trigger_file.resolve()}) does not exist. nothing to do.')
        return
    input_directory.trigger_file.unlink()
    logger.info('start process since trigger file exists')
    input_file = InputFile(input_directory)

    work_directory = WorkDirectory()
    work_input_file = WorkInputFile(input_file, work_directory)

    output_directory = OutputDirectory()
    output_directory.trigger_file.unlink(missing_ok=True)

    result_file = ResultFile(output_directory, work_directory)
    result_file.create(work_input_file)
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
