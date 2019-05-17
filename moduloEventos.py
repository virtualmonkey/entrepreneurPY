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

def getUsers(usersDictionary):
    singleUser = {}
    eventsiWillAssit = []
    with open('usuarios.csv', encoding='utf-8') as f:
        texto = f.read()
    f.close()
    lines = texto.split('\n')
    lines.pop()

    with open('asist.csv', encoding='utf-8') as f:
        texto = f.read() #leer el contenido completo
    f.close()
    asistenciaLines = texto.split('\n')
    asistenciaLines.pop()


    
    for x  in range (0, len(lines)):
        line = lines[x]
        fields = line.split(',')
        for y in range (0, len(asistenciaLines)):
            asistenciaLine = asistenciaLines[y]     
            fieldsAsistencias = asistenciaLine.split(',')
            if (fieldsAsistencias[0] == fields[1]):
                for i in range (1, len(fieldsAsistencias)):
                    eventsiWillAssit.append(fieldsAsistencias[i])
                    print(eventsiWillAssit)
    
        singleUser["name"]=fields[0]
        singleUser["mail"] = fields[1]
        singleUser["age"] = fields[2]
        singleUser["password"] = fields[3]
        singleUser["match"] = fields[4]
        singleUser["eventsToAssist"] = eventsiWillAssit
        #print(singleUser)
        eventsiWillAssit = []
        usersDictionary[singleUser["mail"]] = singleUser
        singleUser = {}

def getEvents(allEventsDictionary):
    with open('eventos.csv', encoding='utf-8') as f:
        texto = f.read()
    f.close()
    lines = texto.split('\n')
    lines.pop()
    for x  in range (0, len(lines)):
        line = lines[x]
        fields = line.split(',')
        newEvent = {
            "eventName" : fields[0],
            "eventCreatorName" : fields[1],
            "eventCreatorMail": fields[2],
            "eventDirection": fields[3],
            "eventDate": fields[4],
            "eventHour": fields[5],
            "eventType": fields[6],
            "eventKey": fields[7]
        }
        allEventsDictionary[newEvent["eventKey"]] = newEvent
        newEvent = {}


def saveEvents(allEventsDictionary):
    filename = "eventos.csv"
    # opening the file with w+ mode truncates the file
    f = open(filename, "w+")
    f.close()


    for generatedKey, value in allEventsDictionary.items():
        with open('eventos.csv', 'a', encoding='utf-8') as f:
            nuevaLinea = value["eventName"] + "," + value["eventCreatorName"] + "," + value["eventCreatorMail"] + "," + value["eventDirection"]  +  "," + value["eventDate"] + "," + value["eventHour"] + "," + value["eventType"] + "," + value["eventKey"] +"\n"
            f.write(nuevaLinea) #escribir
        f.close()
def saveUsers(allUsersDictionary):
    filename = "usuarios.csv"
    # opening the file with w+ mode truncates the file
    f = open(filename, "w+")
    f.close()

    for generatedKey, value in allUsersDictionary.items():
        with open('usuarios.csv', 'a', encoding='utf-8') as f:
            nuevaLinea = value["name"] + "," + value["mail"] + "," + str(value["age"]) + "," + value["password"]  +  "," + value["match"] +"\n"
            f.write(nuevaLinea) #escribir
        f.close()

def saveAsists(allUsersDictionary):
    validation = False
    with open('asist.csv', encoding='utf-8') as f:
        texto = f.read() #leer el contenido completo
    f.close()

    lineas = texto.split('\n')

    lineas.pop()
    for linea in lineas:
        #columnas = linea.split(',')
        #losPerros.append(columnas)
        print(linea)

    nuevaLinea = ""
    filename = "asist.csv"
    # opening the file with w+ mode truncates the file
    f = open(filename, "w+")
    f.close()

    for linea in lineas:
        linea += "\n"
        with open('asist.csv', 'a', encoding='utf-8') as f:
            f.write(linea)
        f.close()
    for generatedKey, value in allUsersDictionary.items():
        print(generatedKey)
        if (validation == False):
            if (len(value["eventsToAssist"]) > 0):
                with open('asist.csv', 'a', encoding='utf-8') as f:
                    print(value)
                    nuevaLinea += value["name"]
                    for val in value["eventsToAssist"]:
                        nuevaLinea += ","
                        nuevaLinea += val
                    nuevaLinea += "\n"
                    print(nuevaLinea)
                    f.write(nuevaLinea) #escribir
                    validation = True
                f.close()
    

        


