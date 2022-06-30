import logging
import logging.config

from processor.ingest import FileReader
from processor.persist import PersistData


class DriverProgram:
    logging.config.fileConfig('./processor/resources/configs/logging.conf')

    def __init__(self, file_type):
        logging.debug('I am within the constructor')
        self.file_type = file_type

    def my_function(self):
        logging.debug(f'inside my function. Processing {self.file_type} file')
        reader = FileReader(self.file_type)
        read_json = reader.read_file()
        print(f'read the json {read_json}')

        writer = PersistData('Postgres')
        writer.store_data(read_json)


if __name__ == '__main__':
    driver = DriverProgram('jso')
    driver.my_function()
