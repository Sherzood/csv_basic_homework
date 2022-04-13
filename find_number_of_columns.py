def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    import csv
    f=open('data.csv')
    data=csv.reader(f)
    l1=[]
    for columns in data:
        l1.append(columns)

    return len(l1)



# Read the csv file