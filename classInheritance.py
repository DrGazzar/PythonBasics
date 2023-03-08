#This script shows how to demonestrate python classes inheritance (OOP)
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics

class genericServer:
    serverName = 'generic'
    serverType = 'generic type'

    def __init__(self):
        print('Initializing generic server ....')

    def __str__(self):
        return self.serverName+'   '+self.serverType

    def setServerName(self, name):
        self.serverName = name

aGeneric = genericServer()

#Inherited class

class webServer(genericServer):
    def getServerName(self):
        return self.serverName


aWebServer = webServer()

aWebServer.setServerName("Web Server # 1")

print("The child is **** ", aWebServer.getServerName(),"***")
