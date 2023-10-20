import csv

#Only Read de csv file
def read_csv(path):
    with open(path, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        
        for row in reader:
            print("***" * 5)
            print(row)