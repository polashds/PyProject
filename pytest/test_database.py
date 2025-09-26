
import unittest
class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.connection = create_test_connection()
        self.cursor = self.connection.cursor()

    def tearDown(self):
        self.cursor.close()
        self.connection.close()

    def test_query(self):
        result = self.connection.query("SELECT 1")
        self.assertEqual(result, 1)