import matplotlib.pyplot as plt 
def findEvent(allEventsDictionary, generatedKey):
    if (generatedKey in allEventsDictionary):
        return True
    return False

def saveEvent(allEventsDictionary, newEvent, generatedKey):
    if(findEvent(allEventsDictionary, generatedKey) == False):
        allEventsDictionary[generatedKey] = newEvent
        return True
    return False

def showGraphic(dataToShowDictionary):    
    # heights of bars 
    height = [v for k,v in dataToShowDictionary.items()]

    # labels for bars 
    tick_label = [k for k,v in dataToShowDictionary.items()] 
    
    # plotting a bar chart 
    plt.bar(range(len(tick_label)), height, color =['purple','yellow']) 
    
    #rotación de las etiquetas a 90 grados
    plt.xticks(range(len(tick_label)), tick_label, rotation = 90)
    # naming the x-axis 
    plt.xlabel('Áreas de emprendimiento') 
    # naming the y-axis 
    plt.ylabel('Socias Actuales') 
    # plot title 
    plt.title('Gráfica de socias por área utilizando FemmeEmpreneur')
    
    # function to show the plot 
    plt.show()  
    
