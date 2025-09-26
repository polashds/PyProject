import sqlite3
import unittest
class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()

    def tearDown(self):
        self.cursor.close()
        self.connection.close()

    def test_query(self):
        self.cursor.execute("SELECT 1")
        result = self.cursor.fetchone()[0]
        self.assertEqual(result, 1)