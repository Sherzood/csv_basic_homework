def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    
    

    for row in data:
        columns=len(row)
    

    return columns



# Read the csv file
import csv
f=open('data.csv')
data=csv.reader(f)
