#This script shows how to demonstrate how to make data type conversions
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)


webServerID = "5495"

type(webServerID)  #this will show that the type of the variable is string

intWebServerID = int(webServerID)

type(intWebServerID) #type converted to integer and can use it in mathematical operations

nextID = intWebServerID + 1

print('The value of the ID is ', intWebServerID)
print('The value of the next ID is ',nextID)

