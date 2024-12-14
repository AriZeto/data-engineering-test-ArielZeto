import unittest
from data_pipeline import read_csv, find_empty_rows
import random

class TestDataPipeline(unittest.TestCase):

    def test_csv_read(self):
        """
        Tests to see if the csv file can be read.
        """
        read_data = read_csv()

        grab_column_names = read_data[0].keys() # Grab the column names for checking if test passes.
        
        # Select some randomized rows from the csv file, given the absurd length of the file.
        random_rows = random.sample(read_data, 50)

        # Check if rows selected match
        for row in random_rows:
            for name in grab_column_names:
                self.assertIn(name, row, "Column not found in the row selected.")


    def test_find_empty_rows(self):
        """
        Tests to determine if the function can find empty rows.
        """
        read_data = read_csv()
        empty_rows = find_empty_rows(read_data)
        self.assertGreater(len(empty_rows), 0, "No empty rows found in the csv file.")

if __name__ == "__main__":
    unittest.main()