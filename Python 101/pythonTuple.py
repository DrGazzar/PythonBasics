#This script shows how to demonestrate tuples in Python
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics

#Tuples items cannot be changes (unlike the list ) - Also, the order cannot be changed
#Tuples allows different data types in the same tuple

classItems = ('pen', 'pencil', 'eraser')

print(classItems)

studentNames = ('Ashraf', 'Sameer', 'Yacoub', 'Sameer')

print(studentNames)

#we can get the length of the tuple using the len function

print(len(studentNames))

#Different data types

mathCourseItemCount = ('pencil', 3, 'pen', 0)

print(mathCourseItemCount)

#tuple is zero indexed

print(classItems[0]) #will pring pen

#Tuple items cannot be changed so that it has to be convered into a list

listClassItems = list(classItems)

listClassItems[0] = 'notebook'
print(listClassItems[0])


# Tuples can be joined together 

anotherClassItems = ('book', 'sheet')

completeClassList = classItems + anotherClassItems

print(completeClassList)

# As it allows duplicates, we can count the number of occurences of an item in a tuple

print(completeClassList.count('sheet'))

