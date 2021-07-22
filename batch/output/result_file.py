import gzip
import csv
import math
import shutil

from output.output_directory import OutputDirectory
from work.work_directory import WorkDirectory
from work.work_input_file import WorkInputFile
from app_name import APP_NAME
from logging import getLogger

logger = getLogger(APP_NAME).getChild(__name__)


class ResultFile:

    def __init__(self, output_directory: OutputDirectory, work_directory: WorkDirectory):
        self.__path = output_directory.path.joinpath('result.csv')
        self.work_file = work_directory.path.joinpath(f'{self.__path.name}.gz')
        logger.debug(f'result file: {self.__path.resolve()}')

    @property
    def path(self):
        return self.__path

    def create(self, work_input_file: WorkInputFile):
        self.write_to_work(work_input_file)
        self.copy_to_actual()
        logger.info(f'created result file')

    def write_to_work(self, work_input_file: WorkInputFile):
        with gzip.open(work_input_file.path, 'rt', newline='') as input_file, gzip.open(self.work_file, 'wt', newline='') as target_file:
            reader = csv.DictReader(input_file, fieldnames=['id', 'purchase_amount'])
            writer = csv.DictWriter(target_file, fieldnames=['id', 'point'])
            for row in reader:
                result_row = {
                    'id': row['id'],
                    'point': math.floor(int(row['purchase_amount']) * 0.01)
                }
                writer.writerow(result_row)

    def copy_to_actual(self):
        with gzip.open(self.work_file, 'rb') as source_file, open(self.path, 'wb') as target_file:
            shutil.copyfileobj(source_file, target_file)