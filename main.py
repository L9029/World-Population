from func import *
import os

def main():
    path = os.path.join(os.getcwd(), "resources/data.csv")
    
    read_csv(path)

if __name__ == "__main__":
    main()