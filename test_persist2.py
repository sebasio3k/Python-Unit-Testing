from processor.persist import PersistData


def test_my_test():
    assert 3 == 3

def test_read_from_pg():
    dbObject = PersistData('postgres')
    courses = dbObject.read_from_pg('futurexschema.futurex_course_catalog')
    print(courses[0][1])
    assert 5 == len(courses[0])