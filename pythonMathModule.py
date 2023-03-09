#This script shows how to demonestrate the math module in python (Math module includes extensive math functions)
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics


import math

#Getting the square root of a value

squareArea = 64

lengthOfTheEdge = math.sqrt(squareArea)

print("The length of the edge is: ", lengthOfTheEdge)


#Using Pi

radius = 10

areaOfTheCircle = math.pi * pow(radius, 2)

print("The area of the circle is: ", areaOfTheCircle)

#Using cos

numValue = 50

cosineValue = math.cos(numValue)

print("cosine is: ", cosineValue)