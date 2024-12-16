import unittest
from data_pipeline import read_csv, fill_empty_cell, remove_leading_zeros, combine_month_year, remove_whitespace, write_csv_changes, remove_dups
import random

class TestDataPipeline(unittest.TestCase):

    # Sets up the required and applied transformations for the data pipeline unit testing.
    def setUp(self):
        # Reads the CSV data.
        self.read_data = read_csv()
        self.grab_column_names = self.read_data[0].keys() # Get column names for checking if test passes.
        self.random_rows = random.sample(self.read_data, 50) # Sample 50 random rows from the data.
        self.write_changes_final_csv = write_csv_changes(self.read_data, "test_write_data.csv") # Write final changes to a new CSV file.


    ##### The following test case is for the read_csv function. #####
    def test_csv_read(self):
        grab_column_names = self.grab_column_names # Grab the column names for checking if test passes.
        
        # Select some randomized rows from the csv file, given the absurd length of the file.
        random_rows = self.random_rows

        # Check if rows selected match
        for row in random_rows:
            for name in grab_column_names:
                self.assertIn(name, row, "Column not found in the row selected.")


    ##### The following tests are for the fill_empty_cell function. #####
    def test_fill_empty_cell_none(self):
        mock_row = {'cell name': None}
        fill_empty_cell(mock_row, 'cell name')
        self.assertEqual(mock_row['cell name'], 'N/A')

    def test_fill_empty_cell_whitespace(self):
        mock_row = {'cell name': '   '}
        fill_empty_cell(mock_row, 'cell name')
        self.assertEqual(mock_row['cell name'], 'N/A')

    def test_fill_empty_cell_empty_string(self):
        mock_row = {'cell name': ''}
        fill_empty_cell(mock_row, 'cell name')
        self.assertEqual(mock_row['cell name'], 'N/A')

    def test_fill_empty_cell_on_non_empty_cell(self):
        mock_row = {'cell name': 'value'}
        fill_empty_cell(mock_row, 'cell name')
        self.assertEqual(mock_row['cell name'], 'value')


    ##### The following tests are for the remove_leading_zeros function. #####
    def test_remove_leading_zeros_with_leading_zero(self):
        mock_row = {'cell name': '0612'}
        remove_leading_zeros(mock_row, 'cell name')
        self.assertEqual(mock_row['cell name'], '612')

    def test_remove_leading_zeros_with_multiple_leading_zeroes(self):
        mock_row = {'cell name': '000612'}
        remove_leading_zeros(mock_row, 'cell name')
        self.assertEqual(mock_row['cell name'], '612')

    def test_remove_leading_zeros_with_just_zero(self):
        mock_row = {'cell name': '0'}
        remove_leading_zeros(mock_row, 'cell name')
        self.assertEqual(mock_row['cell name'], '0')

    def test_remove_leading_zeros_with_no_zeros(self):
        mock_row = {'cell name': '612'}
        remove_leading_zeros(mock_row, 'cell name')
        self.assertEqual(mock_row['cell name'], '612')


    ##### The following tests are for combine_month_year function. #####
    def test_combine_month_year(self):
        mock_rows = [{'Mo Sold': '06', 'Yr Sold': '1994'}, {'Mo Sold': '07', 'Yr Sold': '1995'}]
        
        combine_month_year(mock_rows)

        row = mock_rows[0]
        self.assertNotIn('Mo Sold', row, "Column: Mo Sold located in the data.")
        self.assertNotIn('Yr Sold', row, "Column: Yr Sold column located in the data.")
        self.assertIn('Date When Sold', row, "Column: Date When Sold not located in the data.") 
        self.assertEqual(row['Date When Sold'], '06/1994', "Date When Sold column not properly combined.")


    ##### The following test is for remove_whitespace function. #####
    def test_remove_whitespace(self):
        mock_row = {'cell name': '  value  '}
        remove_whitespace(mock_row, 'cell name')
        self.assertEqual(mock_row['cell name'], 'value')

    ##### The following test is for rem_dups function. #####
    def test_rem_dups(self):
        mock_data = [
            {'abc': '123', 'def': '456'},
            {'abc': '612', 'def': '612'},
            {'abc': '123', 'def': '456'}
        ]
        expected_after_removal = [
            {'abc': '123', 'def': '456'},
            {'abc': '612', 'def': '612'}
        ]

        data_after_removal = remove_dups(mock_data)

        self.assertEqual(data_after_removal, expected_after_removal, "Duplicates were not removed from the data.")
    
    ##### The following test is for test_write_csv_changes function. #####
    def test_write_csv_changes(self):
        write_changes_final_csv  = self.write_changes_final_csv

        # Make sure the file writes using the prior functions, otherwise provide error msg.
        try:
            with open("test_write_data.csv", "r") as file:
                self.assertIsNotNone(file, "File was not written!")
        except FileNotFoundError:
            self.fail("File could not be located...")


if __name__ == "__main__":
    unittest.main()