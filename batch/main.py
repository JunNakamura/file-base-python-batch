from pathlib import Path
import yaml
from logging import config, getLogger
from app_name import APP_NAME
from input.input_directory import InputDirectory
from work.work_directory import WorkDirectory

logger = getLogger(APP_NAME).getChild(__name__)


def main():
    logger.info('start sample batch')
    input_directory = InputDirectory()
    work_directory = WorkDirectory()
    logger.info('processed')
    work_directory.remove_if_exists()


if __name__ == '__main__':
    Path('logs').mkdir(exist_ok=True)
    logging_config_file = Path('logging.yaml')
    with logging_config_file.open() as f:
        log_dict_config = yaml.safe_load(f)
        config.dictConfig(log_dict_config)
    main()
