def findEvent(allEventsDictionary, generatedKey):
    if (generatedKey in allEventsDictionary):
        return True
    return False

def saveEvent(allEventsDictionary, newEvent, generatedKey):
    if(findEvent(allEventsDictionary, generatedKey) == False):
        allEventsDictionary[generatedKey] = newEvent
        return True
    return False
    
