import unittest

from processor.persist import PersistData


class PersistDataTest(unittest.TestCase):

    def test_read_from_pg(self):
        dbObject = PersistData('postgres')
        courses = dbObject.read_from_pg('futurexschema.futurex_course_catalog')
        print(courses[0][1])
        self.assertEqual(courses[0][1], 'Hadoop Sparkddd')

    # def test_first_test(self):
    #     self.assertEqual(3, 3)
    #
    # def test_second_test(self):
    #     self.assertTrue("PYTHON".isupper())
    #
    # def test_third_test(self):
    #     self.assertTrue("python".isupper())


if __name__ == '__main__':
    unittest.main()
