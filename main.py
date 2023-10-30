from func import *
import os

def main():
    path = os.path.join(os.getcwd(), "resources/data.csv")
    
    data = read_csv(path)
    
    #Selection
    selection = input(
    """What kind of chart do you want to generate?
    
    1. Country Population
    2. Population Percentage
        
    type a number: """)
    
    if selection == "1":
        labels, values, country = get_country_population(data)
        bar_chart(labels[::-1], values[::-1], country)
        
    elif selection == "2":
        labels, values = get_country_Population_Percentage(data)
        pie_chart(labels, values)
    
    else:
        print("\n...Something went wrong, please try again...\n")
        print("..Exit...\n")

if __name__ == "__main__":
    main()