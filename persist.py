import logging
import logging.config
import configparser


class PersistData:
    logging.config.fileConfig('./resources/configs/logging.conf')
    logger = logging.getLogger('Persist')
    config = configparser.ConfigParser()
    config.read('./resources/fileprocessor.ini')

    def __init__(self, db_type):
        self.logger.debug('I am within PersistData constructor')
        self.db_type = db_type

    def store_data(self):
        try:
            target_table = self.config.get('DATABASE_CONFIGS', 'PG_TABLE')
            self.logger.debug(f'Target table is {target_table}')
            self.logger.debug(f'Storing data to {self.db_type} ...')
        except Exception as e:
            self.logger.error(f'An error has occured: {e} {type(e)}')
