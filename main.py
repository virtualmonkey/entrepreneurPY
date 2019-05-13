# main.py archive is the principal controller of all the logic of the app
from moduloPerfilesYValidaciones import *
#quiniela = {"Argentina" : ["Luis", "Adriana", "Leslie"], "Alemania" : ["Pedro", "Helena", "María", "Pablo"]  #
#, "Brasil" : ["Marlene", "Ricardo"]}#Creación del diccionario con los datos iniciales       
#dictionary type variables
currentUserDictionary = {}
allUsersDictionary = {}

skillsPointsDictionary = {
    "Costura/Manufactura" : 2, 
    "Deportes" : 3, 
    "Matemática/Programación" : 5, 
    "Emprendimiento/Speaking" : 5, 
    "Economía/Organización" : 4, 
    "Tecnología/Procesos": 5, 
    "Cocina" : 3, 
    "Pintura/Dibujo": 2, 
    "Canto/Danza" : 2, 
    "Adaptación en diferentes Lugares y Culturas": 2

}
areasPointsNeededDictionary = {
    "Moda y Estilo": 8, 
    "Salud y Bienestar": 7, 
    "Tecnología": 12, 
    "Negocios" : 13, 
    "Administración": 9, 
    "Industria": 10, 
    "Gastronomía": 7, 
    "Arte": 7, 
    "Música": 6, 
    "Turismo": 6
}


#Posteriormente hay que hacer un diccionario que contenga como key el nombre de la skill, y el peso que tienen
#También un diccionario que k = Nombre del area, v = puntos necesarios, para realizar el algoritmo del match
skillsList = ["Costura/Manufactura", "Deportes", "Matemática/Programación", "Emprendimiento/Speaking", "Economía/Organización", "Tecnología/Procesos", "Cocina", "Pintura/Dibujo", "Canto/Danza", "Adaptación en diferentes Lugares y Culturas"]
areasList = ["Moda y Estilo", "Salud y Bienestar", "Tecnología", "Negocios", "Administración", "Industria", "Gastronomía", "Arte", "Música", "Turismo"]

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
                    print("Opción 1")
                elif (menuSelection == 2):# Ver eventos a los que asistiré
                    print("Opción 2")
                elif (menuSelection == 3): #Ver eventos creados por mí
                    print("Opción 3")
                elif (menuSelection == 4): #Agregar un evento
                    print("Opción 4")
                elif (menuSelection == 5): #Ver estadísticas de emprendimiento a nivel nacional
                    print("Opción 5")
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
                    mail = input("Ingresa tu dirección de correo: ")
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
                            currentUserDictionary = {
                                "name": name,
                                "mail": mail,
                                "age": age,
                                "password" : password,
                                "skillList": usersSkillsList,
                                "areasList": userAreasList,
                                "match": matchString
                                }
                            allUsersDictionary[mail] = currentUserDictionary
                            isLoggedIn = True
                            print("Te has registrado correctamente!")
                        else:
                            print("La edad debe ser un número, intente de nuevo!")
                    else:
                        print("El correo ya pertenece a una cuenta! Intenta ingresar seleccionando Login en el menú")

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
                    print("Saliendo del programa")
                    currentUserDictionary = {}
                    continueExecuting = 0
            else:
                print("Porfavor ingrese un número entre 1 y 6")
        else:
            print("Porfavor ingrese sólo números")    
