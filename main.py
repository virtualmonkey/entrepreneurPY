# main.py archive is the principal controller of all the logic of the app
from moduloEventos import *
from moduloPerfilesYValidaciones import *
currentUserDictionary = {}
allUsersDictionary = {}
allEventsDictionary ={}

getUsers(allUsersDictionary)
getEvents(allEventsDictionary)
skillsPointsDictionary = {
    "Costura/Manufactura" : 2, 
    "Deportes" : 3, 
    "Matematica/Programacion" : 5, 
    "Emprendimiento/Speaking" : 5, 
    "Economia/Organizacion" : 4, 
    "Tecnologia/Procesos": 5, 
    "Cocina" : 3, 
    "Pintura/Dibujo": 2, 
    "Canto/Danza" : 2, 
    "Adaptacion en diferentes Lugares y Culturas": 2

}
areasPointsNeededDictionary = {
    "Moda y Estilo": 8, 
    "Salud y Bienestar": 7, 
    "Tecnologia": 12, 
    "Negocios" : 13, 
    "Administracion": 9, 
    "Industria": 10, 
    "Gastronomia": 7, 
    "Arte": 7, 
    "Musica": 6, 
    "Turismo": 6
}

dataToShow = {
    "Moda y Estilo": 0, 
    "Salud y Bienestar": 0, 
    "Tecnologia": 0, 
    "Negocios" : 0, 
    "Administracion": 0, 
    "Industria": 0, 
    "Gastronomia": 0, 
    "Arte": 0, 
    "Musica": 0, 
    "Turismo": 0
}


#Posteriormente hay que hacer un diccionario que contenga como key el nombre de la skill, y el peso que tienen
#También un diccionario que k = Nombre del area, v = puntos necesarios, para realizar el algoritmo del match
skillsList = ["Costura/Manufactura", "Deportes", "Matematica/Programacion", "Emprendimiento/Speaking", "Economia/Organizacion", "Tecnologia/Procesos", "Cocina", "Pintura/Dibujo", "Canto/Danza", "Adaptacion en diferentes Lugares y Culturas"]
areasList = ["Moda y Estilo", "Salud y Bienestar", "Tecnologia", "Negocios", "Administracion", "Industria", "Gastronomia", "Arte", "Musica", "Turismo"]
myEventsList = []
#boolean type variables

isLoggedIn = False #variable that saves isLoggedInState

#int type variables
continueExecuting=1 #to while management
menuSelection = 0


#string type variables
menu = ""
while continueExecuting!=0:
   
    menu = getMenu(isLoggedIn)
    print(menu)        
    if (isLoggedIn):
        menuSelection = input("Por favor selecciona una opción del menú: ")
        if (validateNumber(menuSelection)):
            menuSelection = int(menuSelection)
            if (optionInRange(menuSelection, 1, 6)):
                if (menuSelection == 1): #Ver eventos colgados por otras socias
                    eventsThatMatch = [v for k,v in allEventsDictionary.items() if ((v["eventType"]) == currentUserDictionary["match"] and v["eventCreatorMail"] != currentUserDictionary["mail"])]
                    for i in range (len(eventsThatMatch)):
                        print(str(i+1) + " Nombre del evento: " + eventsThatMatch[i]["eventName"])
                        print("   Creado Por: " + eventsThatMatch[i]["eventCreatorName"])
                        print("   Mail de Contacti: " + eventsThatMatch[i]["eventCreatorMail"])
                        print("   Dirección: " + eventsThatMatch[i]["eventDirection"])
                        print("   Fecha de Inicio: " + eventsThatMatch[i]["eventDate"])
                        print("   Hora de Inicio: " + eventsThatMatch[i]["eventHour"])
                        print("   Apto para emprendedoras del área de: " + eventsThatMatch[i]["eventType"])
                        print("\n")
                    eventoSeleccionado = input("Ingrese el número del evento al que desea asistir, ingrese 0 si no desea asistir a ninguno:")
                    if(validateNumber(eventoSeleccionado)):
                        eventoSeleccionado = int(eventoSeleccionado)
                        if(optionInRange(eventoSeleccionado, -1 ,len(eventsThatMatch))):
                            if (eventoSeleccionado != 0):
                                if(eventsThatMatch[eventoSeleccionado-1]["eventKey"] in currentUserDictionary["eventsToAssist"]):
                                    print("Ya asistirás a este evento!")
                                else:
                                    currentUserDictionary["eventsToAssist"].append(eventsThatMatch[eventoSeleccionado-1]["eventKey"])
                                    print("Ahora estás en la lista de asistencia de le evento: " + eventsThatMatch[eventoSeleccionado-1]["eventName"])
                        else:
                            print("El numero especificado está fuera del rango de opciones")
                    else:
                        print("Porfavor ingrese un numero de evento válido")
                elif (menuSelection == 2):# Ver eventos a los que asistiré 
                    print(currentUserDictionary["eventsToAssist"])
                    eventsIWillAssistTo = [v for k,v in allEventsDictionary.items() if (v["eventKey"] in currentUserDictionary["eventsToAssist"])]
                    if (len(eventsIWillAssistTo) != 0):
                        for i in range (len(eventsIWillAssistTo)):
                            print(str(i+1) + " Nombre del evento: " + eventsIWillAssistTo[i]["eventName"])
                            print("   Creado Por: " + eventsIWillAssistTo[i]["eventCreatorName"])
                            print("   Mail de Contacti: " + eventsIWillAssistTo[i]["eventCreatorMail"])
                            print("   Dirección: " + eventsIWillAssistTo[i]["eventDirection"])
                            print("   Fecha de Inicio: " + eventsIWillAssistTo[i]["eventDate"])
                            print("   Hora de Inicio: " + eventsIWillAssistTo[i]["eventHour"])
                            print("   Apto para emprendedoras del área de: " + eventsIWillAssistTo[i]["eventType"])
                            print("\n")

                
                elif (menuSelection == 3): #Ver eventos creados por mí
                    myEventsList = [v for k,v in allEventsDictionary.items() if (v["eventCreatorName"]) == currentUserDictionary["name"]]
                    for i in range (len(myEventsList)):
                        print(str(i+1) + " Nombre del evento: " + myEventsList[i]["eventName"])
                        print("   Creado Por: " + myEventsList[i]["eventCreatorName"])
                        print("   Mail de Contacto: " + myEventsList[i]["eventCreatorMail"])
                        print("   Dirección: " + myEventsList[i]["eventDirection"])
                        print("   Fecha de Inicio: " + myEventsList[i]["eventDate"])
                        print("   Hora de Inicio: " + myEventsList[i]["eventHour"])
                        print("   Apto para emprendedoras del área de: " + myEventsList[i]["eventType"])
                        print("\n")
                elif (menuSelection == 4): #Agregar un evento
                    eventName = input("Ingrese el nombre del evento a guardar: ")
                    eventCreatorName = currentUserDictionary["name"]
                    eventCreatorMail = currentUserDictionary["mail"]
                    eventDirection = input("Ingrese la dirección del evento (puede contener números y letras): ")
                    eventDate = input("Ingrese la fecha en formato DD-MM-AAAA: ")
                    eventHour = input("Ingrese la hora en formato de 24 horas HH:MM: ")
                    eventType = currentUserDictionary["match"]
                    newEvent = { 
                        "eventName" : eventName,
                        "eventCreatorName" : eventCreatorName,
                        "eventCreatorMail": eventCreatorMail,
                        "eventDirection": eventDirection,
                        "eventDate": eventDate,
                        "eventHour": eventHour,
                        "eventType": eventType,
                        "eventKey": eventName+eventCreatorMail
                    }
                    if (saveEvent(allEventsDictionary, newEvent, eventName+eventCreatorMail)):
                        print("El evento se ha guardado exitosamente!")
                    else:
                        "El Evento con nombre "+ eventName +" y correo especificado ya existe!"
                elif (menuSelection == 5): #Ver estadísticas de emprendimiento a nivel nacional
                    showGraphic(dataToShow)
                elif (menuSelection == 6):#Cerrar sesión 
                    print("Cerrando Sesión")
                    isLoggedIn = False
            else:
                print("Porfavor ingrese un número entre 1 y 6")
        else:
            print("Porfavor ingrese sólo números")
    elif (isLoggedIn == False):
        menuSelection = input("Por favor selecciona una opción del menú: ")
        if (validateNumber(menuSelection)):
            menuSelection = int(menuSelection)
            if (optionInRange(menuSelection, 1, 3)):
                if (menuSelection == 1): #Crear Perfil
                    name = input("Ingresa tu nombre completo: ")
                    if(validateOnlyLetters(name)):
                        mail = input("Ingresa tu dirección de correo: ")
                        if(validateMail(mail)):
                            if(allUsersDictionary.get(mail, 0) == 0):
                                age = input ("Ingresa tu edad: ")
                                if (validateNumber(age)):
                                    age = int(age)
                                    password = input("Ingrese una contraseña para su cuenta: ")
                                    usersSkillsList = []
                                    userAreasList = []
                                    tempSkillsList = skillsList.copy()
                                    tempAreasList = areasList.copy()
                                    selectionIndex = 0
                                    for i in range(4):
                                        print("LISTA DE HABILIDADES")
                                        for i in range (len(tempSkillsList)):
                                            print (str(i+1) +". "+ str(tempSkillsList[i]))
                                        selectionIndex = int(input("Ingresa el número de una habilidad que consideras tener: "))
                                        usersSkillsList.append(tempSkillsList[selectionIndex-1])
                                        tempSkillsList.remove(tempSkillsList[selectionIndex - 1])
                                    for i in range(3):
                                        print("LISTA DE INTERESES")
                                        for i in range (len(tempAreasList)):
                                            print (str(i+1) +". "+ str(tempAreasList[i]))
                                        selectionIndex = int(input("Ingresa el número de tu área de interés: "))
                                        userAreasList.append(tempAreasList[selectionIndex-1])
                                        tempAreasList.remove(tempAreasList[selectionIndex - 1])
                                    
                                    matchString = makeMatch(skillsPointsDictionary, areasPointsNeededDictionary, usersSkillsList, userAreasList)
                                    print("FELICIDADES, TIENES UN MATCH CON EL ÁREA DE " + matchString)
                                    dataToShow[matchString] += 1
                                    currentUserDictionary = {
                                        "name": name,
                                        "mail": mail,
                                        "age": age,
                                        "password" : password,
                                        "match": matchString,
                                        "eventsToAssist" : []
                                        }
                                    allUsersDictionary[mail] = currentUserDictionary
                                    isLoggedIn = True
                                    print("Te has registrado correctamente!")
                                else:
                                    print("La edad debe ser un número, intente de nuevo!")
                            else:
                                print("El correo ya pertenece a una cuenta! Intenta ingresar seleccionando Login en el menú")
                        else:
                            print("Porfavor ingrese un mail válido!")
                    else:
                        print("Porfavor ingrese un nombre formado solo por letras!")
                elif (menuSelection == 2):#Ingresar
                    loginEmail = input("Ingresa el email de la cuenta: ")
                    loginPassword = input("Ingresa la constraseña para la cuenta: ")
                    if (allUsersDictionary.get(loginEmail, 0) != 0):
                        currentUserDictionary = allUsersDictionary.get(loginEmail, 0)
                        if (currentUserDictionary["password"] == loginPassword):
                            print("Has iniciado Sesión exitosamente")
                            isLoggedIn = True
                        else:
                            print("La contraseña provista no es correcta")
                            currentUserDictionary = {}
                    else:
                        print("No existe una cuenta con el correo especificado")
                elif (menuSelection == 3):  #Salir del Programa
                    saveEvents(allEventsDictionary)
                    saveUsers(allUsersDictionary)
                    saveAsists(allUsersDictionary)
                    currentUserDictionary = {}
                    continueExecuting = 0
            else:
                print("Porfavor ingrese un número entre 1 y 6")
        else:
            print("Porfavor ingrese sólo números")
