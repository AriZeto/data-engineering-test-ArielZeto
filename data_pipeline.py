import csv

def read_csv():
    """
    Reads the data from the CSV sample data.
    Takes no parameters.
    Returns a list of dictionaries where the rows with number of columns are the keys and the values are the values of the columns.
    """
    with open('data.csv', 'r') as file:
        data = [] # Array to store data.
        csv_reader = csv.DictReader(file) # Returns each row as a dictionary, stored within a list. Utilizing `DictReader` to ensure transformations can be read via their cell values.
        for row in csv_reader:
            data.append(row)
        return data

def find_empty_rows(data):
    """
    Checks for any missing data within the rows of the CSV file.
    Takes data (a list of dicts containing the data of the CSV file) as the single parameter.`
    Returns an array of rows that are missing data, or a string .
    """
    rows_missing_data = [] # Array to store rows that are missing some data.
    # Traverse through every cell of the data array (containing dicts).
    for row in data:
        for cell in row:
            if row[cell] is None or row[cell] == '': 
                rows_missing_data.append(row) # Append the row to the array if a cell is empty.

    # If there are rows missing data, return the rows missing data.
    if len(rows_missing_data) > 0:
        return rows_missing_data
    else:
        return [] # Return empty array given if there are no rows missing data.
    
def data_insertion(rows_missing_data):
    """
    Implements data per each row that is missing data within the CSV file.
    Takes rows_missing_data (a list containing dictionaries of the rows missing data) as the single parameter.
    Returns an updated array of rows with the missing data filled in.
    """
    # Traverse through the rows missing data.
    for row in rows_missing_data:
        for cell in row:
            if row[cell] is None or row[cell] == '':
                row[cell] = 'N/A'
    return rows_missing_data # Return rows with data filled in.


def fill_missing_rows(data, rows_missing_data):
    """
    Fills the rows missing data with the updated data from `data_insertion` function definition.
    Takes `data` (a list of dictionaries containing the data of the CSV file) and `rows_missing_data` (a list of dictionaries containing the rows missing data) as the parameters.
    Returns the updated data with the missing data filled in.
    """
    for row_empty_cells in rows_missing_data:
        for index, row in enumerate(data):
            if row_empty_cells == row:
                data[index] = row_empty_cells
    return data

def remove_leading_zeros(data):
    """
    This simply removes any leading zeros from the data, except for values that are of length > 1 - such that values actually '0' remain.
    Takes data (a list of dictionaries containing the data of the CSV file) as the single parameter.
    Returns data updated where the leading zeroes have been removed.
    """
    # Traverse through the data.
    for row in data:
        for cell in row:
            if row[cell].startswith('0') and len(row[cell]) > 1: # When the cell starts with 0, and the digit is in the tenths or higher place.
                row[cell] = row[cell].lstrip('0') # Remove the leading zero.
    return data

def combine_month_year(data):
    """
    Combines 'Mo Sold' and 'Yr Sold' into a single column 'Date When Sold'.
    Takes data (a list of dictionaries containing the data of the CSV file) as the single parameter.
    Returns data updated with the 'Date When Sold' column.
    """
    if 'Mo Sold' in data[0] and 'Yr Sold' in data[0]:
        for row in data:
            row['Date When Sold'] = f"{row['Mo Sold']}/{str(row['Yr Sold'])}"
            del row['Mo Sold']
            del row['Yr Sold']
    return data

def remove_whitespace(data):
    """
    Removes any whitespace from the data.
    Takes data (a list of dictionaries containing the data of the CSV file) as the single parameter.
    Returns data where whitespace has been removed.
    """
    for row in data:
        for cell in row:
            row[cell] = row[cell].strip()

def write_csv_changes(data, file_name):
    """
    Writes the changes made to the CSV file.
    Takes data (a list of dictionaries containing the data of the CSV file) and a file_name (string of new file you wish to call) as the parameters.
    Returns the new CSV file with the changes made.
    """
    # Write the csv file.
    with open(file_name, mode='w') as file:
        # Ability to write dictionary into a CSV file, with the fieldnames as the keys of the first row - the column names.
        csv_writer = csv.DictWriter(file, fieldnames=data[0].keys()) 
        # Write the column headers, as well as the rows of data.
        csv_writer.writeheader()
        csv_writer.writerows(data)
    

data = read_csv()

check_data = find_empty_rows(data)

provide_fixes = data_insertion(find_empty_rows(data))

apply_fixes = fill_missing_rows(data, data_insertion(find_empty_rows(data)))

remove_leading_zeros = remove_leading_zeros(data)

combine_data = combine_month_year(data)

remove_whitespace = remove_whitespace(data)

write_csv = write_csv_changes(data, 'applied_changes_data.csv')