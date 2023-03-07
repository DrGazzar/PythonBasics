#This script shows how to declare string variables and apply different operations on them
#License GPL
#Created by: Mohamed ElGazzar

frontEndServer = 'Web Server'
backEndServer = 'DB Server'

#concatenation of string variables .. multiple concatenation (variables and empty spaces)
allServers = frontEndServer + ' ' + backEndServer

#print values
print ('The servers are ', frontEndServer, ' and ', backEndServer)

#different functions that can be applied to strings in python

frontLength = len(frontEndServer)

print('The length of the front end server is ', frontLength)