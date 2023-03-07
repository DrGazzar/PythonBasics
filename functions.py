#This script shows how to declaring and calling functions
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics

#Function without parameters and without return values
#Note the indentation .. It is very important 

def displayWelcomeMsg():
    print('Welcome to Python')
    print('This is a function')

#calling the function
displayWelcomeMsg()

#Function with parameters/arguments and without return values
def displayServerName(sname):
    print('The server name is: ', sname)


displayServerName('Web Server')
displayServerName('DB Server')


#Function with parameters/arguments and with return values

def displayTotalUsedMemory (webMemory, dbMemory):
    #print('The total used memory is : ',webMemory + dbMemory)
    return webMemory + dbMemory

print (displayTotalUsedMemory(1000, 5000))   #The values can be replaced with variables too
print (displayTotalUsedMemory(1900, 1200))   #The values can be replaced with variables too


#

