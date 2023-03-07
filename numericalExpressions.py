#This script shows how to declare numberical variables and apply different expressions on them
#License GPL
# Created by: Mohamed ElGazzar

webServerMemory = 1000
dbServerMemory = 2000
usedWebServerMemory = 300
usedDBServerMemory = 400

#addition example and display the results.
totalMemory = webServerMemory + dbServerMemory
print ("The total memory on both servers is:  ", totalMemory)

#subtraction example and display the results
freeWebServerMemory = webServerMemory - usedWebServerMemory
print ("The free memory on the webserver is is:  ", freeWebServerMemory)


