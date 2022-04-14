import csv
def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    for columns in data:
        return columns[0]
    
    
# Read the csv file
f=open('data.csv')
data=csv.reader(f)
