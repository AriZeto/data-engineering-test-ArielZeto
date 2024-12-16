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

def remove_dups(data):
    """
    This function will remove duplicate rows from the data, if given.
    Takes data (a list of dictionaries containing the data of the CSV file) as the single parameter.
    Returns a list of dictionaries with the duplicate rows removed.
    """
    rows_seen = set()
    rows_that_are_unique = []

    for row in data:
        # Convert the values of the row into a tuple, and check if the tuple is in the set.
        values_from_rows = tuple(row.values()) # Obtain the values from the row being iterated on, have it converted because sets must not have mutable contents.
        # If values are not within the set, append them to both the set and the array.
        if values_from_rows not in rows_seen:
            rows_seen.add(values_from_rows)
            rows_that_are_unique.append(row)
        
    return rows_that_are_unique

def fill_empty_cell(row, cell):
    """
    This function fills all empty cells with 'N/A'.
    Takes row, cell as the parameters.
    """
    # If the cell is empty, replace it with 'N/A'.
    if row[cell] is None or row[cell].strip() == '': # Apply strip method in event of cell with just whitespace.
        row[cell] = 'N/A'

def remove_leading_zeros(row, cell):
    """
    This functions removes any leading zeros from data, except for actual zero values (removes when len(num) > 1).
    Takes row, cell as the parameters.
    """
    if row[cell].startswith('0') and len(row[cell]) > 1: # When the cell starts with 0, and the digit is in the tenths or higher place.
        row[cell] = row[cell].lstrip('0') # Remove the leading zero.

def combine_month_year(data):
    """
    Combines 'Mo Sold' and 'Yr Sold' into a single column 'Date When Sold'.
    Takes data (a list of dictionaries containing the data of the CSV file) as the single parameter.
    """
    # Loop through data, locate particular columns, then combine into a new column and remove the old two columns.
    if 'Mo Sold' in data[0] and 'Yr Sold' in data[0]:
        for row in data:
            row['Date When Sold'] = f"{row['Mo Sold']}/{str(row['Yr Sold'])}"
            del row['Mo Sold']
            del row['Yr Sold']

def remove_whitespace(row, cell):
    """
    Removes any whitespace from the data.
    Takes row, cell as the parameters.
    """
    # Remove whitespace from the cell, removing trailing and leading, concatenating the string, and .strip removes whitespace from the middle of a string in the cell.
    row[cell] = ''.join(row[cell].split())


def write_csv_changes(data, file_name):
    """
    Writes the changes made to the CSV file.
    Takes data (a list of dictionaries containing the data of the CSV file) and a file_name (string of new file you wish to call) as the parameters.
    """
    # Write the csv file, utilize a try catch.
    try:
        with open(file_name, mode='w') as file:
            # Ability to write dictionary into a CSV file, with the fieldnames as the keys of the first row - the column names.
            csv_writer = csv.DictWriter(file, fieldnames=data[0].keys()) 
            # Write the column headers, as well as the rows of data.
            csv_writer.writeheader()
            csv_writer.writerows(data)
    # Catch any errors that may occur.
    except Exception as error:
        print(f"An error occurred when attempting to write the file, see error here: {error}")


def main():
    """
    Main function to execute all validation and transformation upon the data.
    Takes no parameters.
    """
    # Reads the data from CSV file.
    data = read_csv()
    data = remove_dups(data) # Removes duplicate rows, if any, cleaning file.
    # Loop though all the cells in the CSV data.
    for row in data:
        for cell in row:
            fill_empty_cell(row, cell) # Fill empty cells with 'N/A'.
            remove_leading_zeros(row, cell) # Remove leading zeros from the data.
            remove_whitespace(row, cell) # Remove any whitespace from the cell data.
    combine_month_year(data) # Combine 'Mo Sold' and 'Yr Sold' into 'Date When Sold', and remove said prior two columns.
    # Write said transformations and validation to a new CSV file.
    write_csv_changes(data, 'applied_changes_data.csv')

# Call to execute transformations and validation on the data.
if __name__ == "__main__":
    main()