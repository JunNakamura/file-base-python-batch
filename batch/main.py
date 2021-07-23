from pathlib import Path
import yaml
from logging import config, getLogger
from app_name import APP_NAME
from file_base_batch import FileBaseBatch

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
