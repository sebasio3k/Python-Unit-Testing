import logging
import logging.config
import json


class FileReader:
    logging.config.fileConfig('./processor/resources/configs/logging.conf')
    logger = logging.getLogger('Ingest')

    def __init__(self, file_type):
        self.logger.info('I am within FileReader constructor')
        self.file_type = file_type

    def read_file(self):
        self.logger.debug(f'Reading a {self.file_type} file ...')
        with open('./processor/resources/course.json') as file:
            new_course = json.load(file)
        print(f'new_course is {new_course}')
        return new_course
