import matplotlib.pyplot as plt

def bar_chart(labels, values, name):
    fig, ax = plt.subplots()
    ax.bar(labels, values, width=0.6, color="#86bf91")
    
    ax.set_xlabel("Año de Senso", size=10, fontfamily="sans", weight="bold")
    ax.set_ylabel("Poblacion (Millones)", size=10, fontfamily="sans", weight="bold")
    
    plt.xticks(fontsize='8.5', weight='bold', color='#7e807e')
    plt.yticks(fontsize='8.5', weight='bold', color='#7e807e')
    
    #Tile of the Chart
    plt.title("Población de " + name, size=17, weight='bold', fontfamily="serif", color='#598561', horizontalalignment = 'left', x=0.038, y=0.96, transform=fig.transFigure)
    
    #Subtitle of the Chart
    plt.suptitle("Desde el año 1970 al año 2022", size=10, fontfamily="sans", color="#5f615f", weight="bold", horizontalalignment = 'left', x=0.038, y=0.94, transform=fig.transFigure)
    
    plt.show()

def pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis("equal")
    plt.show()