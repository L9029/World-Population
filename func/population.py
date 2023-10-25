def get_country_population(data):
    new_data = []
    x = ["Country/Territory", "2022 Population", "2020 Population", "2015 Population", "2010 Population", "2000 Population", "1990 Population", "1980 Population", "1970 Population"]
    
    for i in data:
        temp = {}
        for j in x:
            temp[j] = i.get(j)
        new_data.append(temp)
    
    return new_data