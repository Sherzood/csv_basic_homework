def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    l=[]
    for row in data:
        l.append(row)
    return len(l)-1      

# Read the csv file
import csv
f=open('data.csv')
data=csv.reader(f)
print(find_number_of_rows(data))
