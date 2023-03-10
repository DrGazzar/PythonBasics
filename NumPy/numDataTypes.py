#This script shows how to demonestrate numpy data types (strings, integers, float, boolean and complex)
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics

import numpy as np

successRate = np.array([100,98,76,84], dtype='f')

print(type(successRate))

print(type(successRate[0]))


#### converting data types , it will remove the fraction.
studentGrades = np.array([90.2, 95.8, 83.9])

modifiedStudentGrades = studentGrades.astype('i')

print(modifiedStudentGrades)
print(type(modifiedStudentGrades[0]))

######### copy and view

newCopy = modifiedStudentGrades.copy()
newCopy[0] = 95

print('The copy is ',newCopy)
print('The original is: ', modifiedStudentGrades)


########## view -- modification impacts the original array

anotherNewCopy = modifiedStudentGrades.view()
anotherNewCopy[0] = 95

print('The copy is ',anotherNewCopy)
print('The original is: ', modifiedStudentGrades)

