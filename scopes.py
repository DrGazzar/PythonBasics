#This script shows how to demonestrate python classes inheritance (OOP)
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics


#Printing the global 

serverName = "ws # 1"
serverType = "web server"


def getName():
    print("The servername is ", serverName)

getName()

def getType():   # will print the local server type
    serverType = "Database server"
    print("The server type is", serverType)


getType()

def getGlobalType():   # will print the global server type (web server)
    global serverType 
    print("The server type is", serverType)

getGlobalType()