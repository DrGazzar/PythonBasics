#This script shows how to declare string variables and apply different operations on them
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)

frontEndServer = 'Web Server'
backEndServer = 'DB Server'

#concatenation of string variables .. multiple concatenation (variables and empty spaces)
allServers = frontEndServer + ' ' + backEndServer

#print values
print ('The servers are ', frontEndServer, ' and ', backEndServer)

#different functions that can be applied to strings in python

frontLength = len(frontEndServer)

print('The length of the front end server is ', frontLength)

#Also there are functions that transforms the strings

# Capitalize the first letter of the string so the output will be       Db server 
print ( backEndServer.capitalize()  )

#  Converts the whole string to small (lower) letters so the output will be       db server 
print ( backEndServer.casefold()  )

