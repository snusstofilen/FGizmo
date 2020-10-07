import pandas as pd
import pdb

from lib.database.database import Database

class Database_CSV(Database):

    def import_data(self):
        self.data = pd.read_csv("lib/database/dataset.csv")

if __name__ == "__main__":
    database = Database_CSV()
    print(database.data.head())
