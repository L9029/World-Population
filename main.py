from func import *
import os

def main():
    path = os.path.join(os.getcwd(), "resources/data.csv")
    
    data = read_csv(path)
    print(data)

if __name__ == "__main__":
    main()