import gzip
import csv
import math
import shutil

from output.output_directory import OutputDirectory
from work.work_directory import WorkDirectory
from work.work_entry_file import WorkEntryFile
from work.work_input_file import WorkInputFile
from app_name import APP_NAME
from logging import getLogger

from work.work_order_history_file import WorkOrderHistoryFile

logger = getLogger(APP_NAME).getChild(__name__)


class ResultFile:

    def __init__(self, output_directory: OutputDirectory, work_directory: WorkDirectory):
        self.__path = output_directory.path.joinpath('result.csv')
        self.work_file = work_directory.path.joinpath(f'{self.__path.name}.gz')
        logger.info(f'result file: {self.__path}')

    @property
    def path(self):
        return self.__path

    def create(self, work_order_history_file: WorkOrderHistoryFile, work_entry_file: WorkEntryFile):
        self.write_to_work(work_order_history_file, work_entry_file)
        self.copy_to_actual()
        logger.info(f'created result file')

    def write_to_work(self, work_order_history_file: WorkOrderHistoryFile, work_entry_file: WorkEntryFile):
        with gzip.open(work_order_history_file.path, 'rt', newline='') as order_history_file, gzip.open(self.work_file, 'wt', newline='') as target_file:
            with gzip.open(work_entry_file.path, 'rt', newline='') as entry_file:
                entries = {line for line in entry_file.read().splitlines()}
                reader = csv.DictReader(order_history_file, fieldnames=['user_id', 'purchase_amount'])
                writer = csv.DictWriter(target_file, fieldnames=['user_id', 'point'])
                for row in reader:
                    if (user_id := row['user_id']) in entries:
                        result_row = {
                            'user_id': user_id,
                            'point': math.floor(int(row['purchase_amount']) * 0.01)
                        }
                        writer.writerow(result_row)

    def copy_to_actual(self):
        with gzip.open(self.work_file, 'rb') as source_file, open(self.path, 'wb') as target_file:
            shutil.copyfileobj(source_file, target_file)