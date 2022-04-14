import csv
def get_first_row(data):  
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
    for first_row in data:
        return first_row[1] 

# Read the csv file
f=open('data.csv')
data=csv.reader(f)
print(get_first_row(data))

