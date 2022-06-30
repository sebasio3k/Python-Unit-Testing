import logging
import logging.config

from processor.ingest import FileReader
from processor.persist import PersistData

from flask import Flask, request

app = Flask(__name__)


@app.route('/courses', methods=['GET'])
def get_courses():
    dbObject = PersistData('postgres')
    courses = dbObject.read_from_pg('futurexschema.futurex_course_catalog')
    return f'Courses are - {courses}'


@app.route('/courses', methods=['POST'])
def insert_course():
    input_json = request.get_json(force=True)
    print(f'input_json > {input_json}')
    dbObject = PersistData('postgres')
    dbObject.write_from_json_to_pg(
        'futurexschema.futurex_course_catalog',
        input_json
    )

    return 'Success'


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
    app.run(port=8005, debug=True)
    # driver = DriverProgram('jso')
    # driver.my_function()
