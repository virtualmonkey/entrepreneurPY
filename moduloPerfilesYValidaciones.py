import random
def validateNumber(numAsString): #Funcion para validar que el dato ingresado por el usuario sea un numero
    try:#Que verifique si:
        int(numAsString)#Se divide el dato ingresado entre uno para verificar que sea un numero, si lo es, se duevuelve True
        return True
    except ValueError:#La excpecion sera un error de valor y retornara falso
        return False
def optionInRange(x, minInRange, maxInRange):#Funcion para validar si un numero x esta dentro de un rango establecido.
    if (x >= minInRange and x <= maxInRange) or (x <= minInRange and x >= maxInRange):#Si x se encuentra dentro del rango de a y maxInRange
        return True#Retornara True
    else:
        return False#De lo contrario retonrara falso
def getMenu(isLoggedIn):


    if (isLoggedIn == True):
        return """ 
                MENU DE OPCIONES
        1. Ver eventos colgados por otras socias
        2. Ver eventos a los que asistiré
        3. Ver eventos creados por mí
        4. Publicar un Evento
        5. Ver estadísticas de emprendimiento a nivel nacional
        6. Cerrar sesión     
        """
    return """ 
                MENU DE OPCIONES
        1. Crear Perfil
        2. Login
        3. Salir del programa    
        """
def makeMatch (skillsPointsDic, areasPointsNeededDic, userSkillsLis, usersAreasLis):
        totalPoints = 0
        randomIndex = random.randint(0,2)
        maxIndex = -1
        matchString = ""
        for i in range (len(userSkillsLis)):
                totalPoints += skillsPointsDic[userSkillsLis[i]]

        if (totalPoints < areasPointsNeededDic[usersAreasLis[0]] and totalPoints < areasPointsNeededDic[usersAreasLis[1]] and totalPoints < areasPointsNeededDic[usersAreasLis[2]]):
                return usersAreasLis[randomIndex]

        for i in range (len(usersAreasLis)):
                if (totalPoints >= areasPointsNeededDic[usersAreasLis[i]]):
                        maxIndex += 1
        
        return usersAreasLis[maxIndex]

def validateOnlyLetters(name):
	if (name.replace(' ','').isalpha()):
		return True
	return False

def validateMail(mail):
	if ("@gmail.com" in mail or "@hotmail.com" in mail or "@outlook.com" in mail or "@yahoo.com" in mail):
			return True
	return False
def validatePassword(password):
	if(len(password) >= 6):
			return True
	return False

