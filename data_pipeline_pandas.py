import pandas as pd

def read_csv():
    """
    Reads the data from the CSV sample data and creates a data frame.
    Takes no parameters.
    Returns the data frame.
    """
    data_frame = pd.read_csv('data.csv', keep_default_na=False)
    return data_frame

def remove_dups(data_frame):
    """
    This function will remove duplicate rows from the data, if given.
    Takes the data frame as the single parameter.
    Returns the data frame with duplicates removed.
    """
    return data_frame.drop_duplicates()

def fill_empty_cells(data_frame):
    """
    This function fills all empty cell values with 'N/A'.
    Takes the data frame as the parameter.
    Returns the data frame with empty cells filled with 'N/A'.
    """
    return data_frame.replace('', 'N/A')

# Pandsa will typically remove leading zeroes, but I designed the function for transformation purposes.
def remove_leading_zeros(data_frame):
    """
    This functions removes any leading zeroes from data, except for actual zero values (removes when len(num) > 1).
    Takes data frame as parameter.
    Returns the data frame with leading zeroes removed.
    """
    # Applies stripping zeros to the data frame when len(num) > 1.
    return data_frame.map(lambda x: str(x).lstrip('0') if isinstance(x, str) and len(str(x)) > 1 else x)

def combine_month_year(data_frame):
    """
    Combines 'Mo Sold' and 'Yr Sold' into a single column 'Date When Sold'.
    Takes the data frame as the single parameter.
    Returns the data frame with those two colummns combined.
    """
    # Combine the two columns into a single column, dubbed 'Date When Sold', cast as specific type of str.
    data_frame['Date When Sold'] = data_frame['Mo Sold'].astype(str) + '/' + data_frame['Yr Sold'].astype(str)
    # Drop original two columns after combining them
    return data_frame.drop(['Mo Sold', 'Yr Sold'], axis=1)

def remove_whitespace(data_frame):
    """
    Removes whitespace from cells.
    Takes the data frame as the only parameter.
    Returns the data frame with whitespace removed.
    """
    # Maps over data frame, removes whitespace from cells.
    return data_frame.map(lambda x: x.replace(' ', '') if isinstance(x, str) else x)

def write_csv_changes(data_frame):
    """
    Writes the changes made to the data frame into a new CSV file.
    Takes the data frame as the parameter.
    """
    data_frame.to_csv('applied_changes_data_panda.csv', index=False)

def main():
    """
    Main function to execute all validation and transformation upon the data.
    Takes no parameters.
    """
    # Read data from CSV file and creates data frame
    data_frame = read_csv()

    data_frame = remove_dups(data_frame) # Removes dup. rows, if exist.
    data_frame = remove_whitespace(data_frame) # Maps over dataframe, removes whitespace from cells.
    data_frame = fill_empty_cells(data_frame) # Fill empty cells with 'N/A'.
    data_frame = remove_leading_zeros(data_frame) # Remove leading zeros.
    data_frame = combine_month_year(data_frame) # Combines two columns into one.
    
    write_csv_changes(data_frame) # Writes changes to the new CSV file.

# Call to execute transformations and validation on the data.
if __name__ == "__main__":
    main()