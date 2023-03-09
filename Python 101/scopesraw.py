#This script shows how to demonestrate the scopes in python
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar) 
#Github repo: https://github.com/DrGazzar/PythonBasics


#Printing the global 

serverName = "ws # 1"
serverType = "web server"


def getName():
    print("The servername is ", serverName)



def getType():   # will print the local server type
    serverType = "Database server"
    print("The server type is", serverType)




def getGlobalType():   # will print the global server type (web server)
    global serverType 
    print("The server type is", serverType)
