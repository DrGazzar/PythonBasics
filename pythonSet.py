#This script shows how to demonestrate lists in Python
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics


#Sets are unorderd and unindexed. 
#cannot update the items but can add and remove
#duplicates are not allowed

serverSet = {'web server', 'application server', 'mail server', 'database server'}

print(serverSet)

#### set operations

#   print(serverSet[1])    ....  this will generate an error because the set is unindexed

# Add items and print the set

serverSet.add('file server')

for server in serverSet:
    print(server)


print ('-------')

# Remove items

serverSet.add('web server')

for server in serverSet:
    print(server)

#Similar to tuples, sets can be joined together using union

applicationSet = {'outlook','apache', 'samba'}

infrastructure = applicationSet.union(serverSet)

print(infrastructure)