import unittest

from pandas.core.frame import DataFrame

from lib.database.database_csv import Database_CSV

class Test_Database_CSV(unittest.TestCase):

    def test_import_data(self):

        database = Database_CSV()
        database.import_data()

        self.assertIsInstance(database.data, DataFrame)
