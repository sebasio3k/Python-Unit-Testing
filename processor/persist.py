import logging
import logging.config
import configparser

import psycopg2

import json


class PersistData:
    logging.config.fileConfig('./processor/resources/configs/logging.conf')
    logger = logging.getLogger('Persist')
    config = configparser.ConfigParser()
    config.read('./processor/resources/fileprocessor.ini')

    def __init__(self, db_type):
        self.logger.debug('I am within PersistData constructor')
        self.db_type = db_type

    def store_data(self, course_json):
        try:
            target_table = self.config.get('DATABASE_CONFIGS', 'PG_TABLE')
            self.logger.debug(f'Target table is {target_table}')
            self.logger.debug(f'Storing data to {self.db_type} ...')
            # self.write_to_pg(target_table)
            # self.read_from_pg(target_table)
            self.write_from_json_to_pg(target_table, course_json)
        except Exception as e:
            self.logger.error(f'An error has occured: {e} {type(e)}')

    def read_from_pg(self, target_table):
        connection = psycopg2.connect(
            user='postgres',
            password='admin',
            host='localhost',
            database='postgres')

        cursor = connection.cursor()

        # select_query = "SELECT * from futurexschema.futurex_course_catalog"
        select_query = "SELECT * from " + target_table

        cursor.execute(select_query)

        # print(cursor.fetchone())
        # print(cursor.fetchall())

        records = cursor.fetchall()
        for item in records:
            print(item)

        cursor.close()
        connection.commit()

        return records

    def write_to_pg(self, target_table):
        connection = psycopg2.connect(
            user='postgres',
            password='admin',
            host='localhost',
            database='postgres')

        cursor = connection.cursor()

        # insert_query = "INSERT into futurexschema.futurex_course_catalog " \
        #                "(course_id, course_name, author_name, course_section, " \
        #                "creation_date) VALUES (%s, %s, %s, %s, %s)"

        print('Inserting to PG')

        cursor.execute("SELECT max(course_id) from " + target_table)
        max_course_id = cursor.fetchone()[0]
        print(f'max_course_id is {max_course_id}')

        insert_query = "INSERT into " + target_table + \
                       "(course_id, course_name, author_name, course_section, " \
                       "creation_date) VALUES (%s, %s, %s, %s, %s)"

        insert_tuple = (max_course_id + 1, 'IA2', 'FutureX', '{}', '2022-06-28')

        cursor.execute(insert_query, insert_tuple)

        cursor.close()
        connection.commit()

    def write_from_json_to_pg(self, target_table, course_json):
        self.logger.debug('Write_from_json_to_pg method started')
        connection = psycopg2.connect(
            user='postgres',
            password='admin',
            host='localhost',
            database='postgres')

        cursor = connection.cursor()

        print('Inserting to PG')

        cursor.execute("SELECT max(course_id) from " + target_table)
        max_course_id = cursor.fetchone()[0]
        print(f'max_course_id is {max_course_id}')

        insert_query = "INSERT into " + target_table + \
                       "(course_id, course_name, author_name, course_section, " \
                       "creation_date) VALUES (%s, %s, %s, %s, %s)"

        insert_tuple = (max_course_id + 1,
                        course_json['course_name'],
                        course_json['author_name'],
                        json.dumps(course_json['course_section']),
                        course_json['creation_date'])

        cursor.execute(insert_query, insert_tuple)

        cursor.close()
        connection.commit()
