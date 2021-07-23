from input.input_directory import InputDirectory
from input.input_file import InputFile


class EntryFile(InputFile):

    def __init__(self, input_directory: InputDirectory):
        super().__init__(input_directory, 'entry.csv')
