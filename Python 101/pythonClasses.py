#This script shows how to demonestrate python classes (OOP)
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics

class serverClass:
    hasDisk = True


dataCenterServer = serverClass()
print(dataCenterServer.hasDisk)

######## constructor ############

class dbEngine:
    def __init__(self, engineType):   #defining a parameter engineType
        self.engineType = engineType
        print("demonestrating the constructor -- ", self.engineType)

    def __str__(self):
        return "displaying the engine type when printing --> the engine type is "+ self.engineType

webDbServer = dbEngine("mysql")


print(webDbServer.engineType)

print('printing the object', webDbServer)


############# object methods can be defined similar to regular functions ###############

class programmingLanguage:
    def __init__(self, name):
        self.name = name
    
    def setOS(self, os):
        self.os = os
    
    def getOS(self):
        return self.os

programmingLang = programmingLanguage("Java")
programmingLang.setOS("All")

print(programmingLang.getOS())


############# deleting an object


del programmingLang