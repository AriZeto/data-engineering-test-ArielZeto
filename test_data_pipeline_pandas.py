import unittest
from unittest.mock import patch, mock_open
import pandas as pd
from pandas.testing import assert_frame_equal
from data_pipeline_pandas import read_csv, fill_empty_cells, remove_leading_zeros, combine_month_year, remove_whitespace, write_csv_changes, remove_dups
import random

class TestDataPipelinePandas(unittest.TestCase):

    # Sets up for the data pipeline unit testing.
    def setUp(self):
        self.mock_basic_data_frame = pd.DataFrame({
            'fruit': ['orange', 'apple'],
            'vegetable': ['celery', 'broccoli']
        })

    ##### The following test case is for the read_csv function. #####
    # Use patch to replace the read_csv function with a mock function.
    @patch('pandas.read_csv')
    def test_read_csv(self, mock_read_csv):
        # Make a mock data frame to simulate what would be returned by pandas.read_csv.
        mock_data_frame = self.mock_basic_data_frame
        
        # Tell our mock pandas.read_csv function to return our mock data frame.
        mock_read_csv.return_value = mock_data_frame
        
        actual_returned_data_frame = read_csv()
        
        # Check that the data frame returned by read_csv is equivalent to mock data frame.
        assert_frame_equal(actual_returned_data_frame, mock_data_frame)
        
        # Ensure our mock pandas.read_csv function was called with the right parameters.
        mock_read_csv.assert_called_once_with('data.csv', keep_default_na=False)


    ##### The following tests are for the fill_empty_cell function. #####
    def test_fill_empty_cells(self):
        mock_data_frame = pd.DataFrame({'soup': ['', 'tomato'], 'rice': ['jasmine', '']})
        expected_after_fill = pd.DataFrame({'soup': ['N/A', 'tomato'], 'rice': ['jasmine', 'N/A']})
        result_data_frame = fill_empty_cells(mock_data_frame)
        assert_frame_equal(result_data_frame, expected_after_fill)

    def test_fill_empty_cells_no_empty(self):
        mock_data_frame = pd.DataFrame({'soup': ['split-pea', 'tomato'], 'rice': ['jasmine', 'basmati']})
        expected_after_fill = pd.DataFrame({'soup': ['split-pea', 'tomato'], 'rice': ['jasmine', 'basmati']})
        result_data_frame = fill_empty_cells(mock_data_frame)
        assert_frame_equal(result_data_frame, expected_after_fill)

    ##### The following tests are for the remove_leading_zeros function. #####
    def test_remove_leading_zeros_with_leading_zero(self):
        mock_data_frame = pd.DataFrame({'col name': ['0612']})
        expected_after_removal = pd.DataFrame({'col name': ['612']})
        result_data_frame = remove_leading_zeros(mock_data_frame)
        assert_frame_equal(result_data_frame, expected_after_removal)

    def test_remove_leading_zeros_with_multiple_leading_zeroes(self):
        mock_data_frame = pd.DataFrame({'col name': ['000612']})
        expected_after_removal = pd.DataFrame({'col name': ['612']})
        result_data_frame = remove_leading_zeros(mock_data_frame)
        assert_frame_equal(result_data_frame, expected_after_removal)

    def test_remove_leading_zeros_with_just_zero(self):
        mock_data_frame = pd.DataFrame({'col name': ['0']})
        expected_after_removal = pd.DataFrame({'col name': ['0']})
        result_data_frame = remove_leading_zeros(mock_data_frame)
        assert_frame_equal(result_data_frame, expected_after_removal)

    def test_remove_leading_zeros_with_no_zeros(self):
        mock_data_frame = pd.DataFrame({'col name': ['612']})
        expected_after_removal = pd.DataFrame({'col name': ['612']})
        result_data_frame = remove_leading_zeros(mock_data_frame)
        assert_frame_equal(result_data_frame, expected_after_removal)


    ##### The following test is for combine_month_year function. #####
    def test_combine_month_year(self):
        mock_data_frame = pd.DataFrame({
            'Mo Sold': ['06', '07'],
            'Yr Sold': ['1994', '1995']
        })
        result_data_frame = combine_month_year(mock_data_frame)
        self.assertNotIn('Mo Sold', result_data_frame.columns, "Column: Mo Sold located in the data.")
        self.assertNotIn('Yr Sold', result_data_frame.columns, "Column: Yr Sold column located in the data.")
        self.assertIn('Date When Sold', result_data_frame.columns, "Column: Date When Sold not located in the data.") 
        self.assertEqual(result_data_frame.loc[0, 'Date When Sold'], '06/1994', "Date When Sold column not properly combined.")

    ##### The following test is for remove_whitespace function. #####
    def test_remove_whitespace(self):
        mock_data_frame = pd.DataFrame({
            'rice': ['  jasmine  ', '  basmati  '],
            'soup': ['split pea,', 'tomato']
        })
        expected_data_frame = pd.DataFrame({
            'rice': ['jasmine', 'basmati'],
            'soup': ['splitpea,', 'tomato']
        })
        result_data_frame = remove_whitespace(mock_data_frame)
        assert_frame_equal(result_data_frame, expected_data_frame)


    ##### The following test is for rem_dups function. #####
    def test_rem_dups(self):
        mock_data_frame = pd.DataFrame({
            'abc': ['123', '456', '123'],
            'def': ['789', '615', '789']
        })
        expected_after_removal = pd.DataFrame({
            'abc': ['123', '456'],
            'def': ['789', '615']
        })
        result_data_frame = remove_dups(mock_data_frame)
        assert_frame_equal(result_data_frame, expected_after_removal, "Duplicates were not removed from the data.")
    
    ##### The following test is for test_write_csv_changes function. #####
    # Use patch to mock the pandas .to_csv method.
    @patch('pandas.DataFrame.to_csv')
    def test_write_csv_changes(self, mock_to_csv):
        data_frame = self.mock_basic_data_frame

        write_csv_changes(data_frame)
        
        # Since we are basically just testing that an internal pandas method was called, we don't need to be too thorough here.
        # Ensure that the method was called with the correct parameters.
        mock_to_csv.assert_called_once_with('applied_changes_data_panda.csv', index=False)

if __name__ == "__main__":
    unittest.main()