from input.input_directory import InputDirectory
from input.input_file import InputFile


class OrderHistoryFile(InputFile):

    def __init__(self, input_directory: InputDirectory):
        super().__init__(input_directory, 'order_history.csv')
