#This script shows how to declare numberical variables and apply different expressions on them
#License GPL
#Created by: Mohamed ElGazzar


webServerMemory = 55340
dbServerMemory = 13420

# check which have higher memory
# Note the indentation .. it is very important

if webServerMemory > dbServerMemory:
    print ('The Web Server has higher memory')
    print ('The value of the memory is --> ', webServerMemory)

# else if statement in python to have some action done if the condition is wrong


if webServerMemory > dbServerMemory:
    print ('The Web Server has higher memory')
    print ('The value of the memory is --> ', webServerMemory)
elif webServerMemory == dbServerMemory:
    print ('Memory in both servers are equal')
else:
    print ('The memory of the DB Server is higher than the memory of the web server')
    print ('The value is -->', dbServerMemory)


# If statements can be nested -- Indentation is very important


#------------------------ The composite conditions -- logical operators -- and ---------------------------

webServerStorage = 55653
dbServerStorage = 3563


if webServerMemory > dbServerMemory and webServerStorage > dbServerStorage:
    print ('Web Server Specifications is higher than the DB server specifications')


#------------------------ The composite conditions -- logical operators -- or  ---------------------------

if webServerMemory > dbServerMemory or webServerStorage > dbServerStorage:
    print ('Web Server has one of the specifications higher than the DB server')


#------------------------ The composite conditions -- logical operators -- not  ---------------------------

if not webServerMemory > dbServerMemory:
    print ('The memory of the DB server is higher than the memory of the web server')

