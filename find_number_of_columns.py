def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    row=data.split('\n')
    columns=len(row[0].split(','))
    
    
    return columns
    
    
    
    




# Read the csv file
f=open('data.csv')
data=f.read()
print(find_number_of_columns(data))

