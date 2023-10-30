#This function filter the csv file to get the country and population by year and return the labels and values.
def get_country_population(data):
    new_data = []
    x = ["Country/Territory", "2022 Population", "2020 Population", "2015 Population", "2010 Population", "2000 Population", "1990 Population", "1980 Population", "1970 Population"]
    
    for i in data:
        temp = {}
        for j in x:
            temp[j] = i.get(j)
        new_data.append(temp)
    
    country = input("\nType a Country: ")
    
    for i in new_data:
        if i["Country/Territory"] == country:
            i.pop("Country/Territory")
            labels = list(i.keys())
            values = [int(i) for i in i.values()]
    
    return labels, values, country

#This function filter the csv file to get the country and population percentage by the continent.
def get_country_Population_Percentage(data):
    continents = ["Asia", "Europe", "Africa", "Oceania", "North America", "South America"]
    
    continent = int(input("""\nChoose a Continent
                          
    1.Asia
    2.Europe
    3.Africa
    4.Oceania
    5.North America
    6.South America
                      
    Type a number: """))
    
    if continent <= 6:
        data = list(filter(lambda item: item['Continent'] == continents[continent-1], data)) #Filter the data by continent
    
        filter_data = []
        x = ["Country/Territory", "World Population Percentage"]

        for i in data:
            temp = {}
            for j in x:
                temp[j] = i.get(j)
            filter_data.append(temp)

        labels = [i.get(x[0]) for i in filter_data] #Countries
        values = [float(i.get(x[1])) for i in filter_data] #Population Percentage
        
        return labels, values
    
    else:
        print("\n...Something went wrong, please try again...\n")
        print("..Exit...\n")