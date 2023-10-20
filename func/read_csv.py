import csv

#Only Read de csv file
def read_csv(path):
    with open(path, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        header = next(reader)
        data = []
        
        for row in reader:
            iterable = zip(header, row)
            #Convert the iterable list in a dictionary with dict comprehension
            csv_dict = {key: value for key, value in iterable}
            data.append(csv_dict)
        
        return data