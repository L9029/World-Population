from func import *
import os

def main():
    path = os.path.join(os.getcwd(), "resources/data.csv")
    
    data = read_csv(path)
    new_data = get_country_population(data)
    
    country = input("Ingrese un Pais: ")
    
    for i in new_data:
        if i["Country/Territory"] == country:
            i.pop("Country/Territory")
            labels = list(i.keys())
            values = [int(i) for i in i.values()]
    
    bar_chart(labels[::-1], values[::-1], country)

if __name__ == "__main__":
    main()