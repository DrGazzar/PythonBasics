#This script shows how to demonestrate numpy random
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics

import numpy as np
from numpy import random


######## Generate random numbers

randomExample = random.randint(100)

print("The generated random integer is: ", randomExample)

randomFloatExample = random.rand()

print("The generated random float is: ", randomFloatExample)

########## Generate number arrays

randomArray = random.randint(100, size=(5))

print("The random array is: ", randomArray)

######## Generate 2 dimentional random array ####

random2DArray = random.randint(100, size=(5,6))

print("The 2 dimensional array is: ", random2DArray)

######### randomly generates one element of the array ########

operatingSystemsList = np.array(["Linux", "Windows", "Unix", "macOS"])

randomFromArray = random.choice(operatingSystemsList)

print("Random element of the array: ", randomFromArray)

########### random from array with probability

randomFromArrayProb = random.choice(operatingSystemsList, p=[0.6,0.1,0.1,0.2])

print("Random element of the array with probability: ", randomFromArrayProb)

########## Shuffle and Permutation ##############


operatingSystemCloneList = operatingSystemsList.copy()
random.shuffle(operatingSystemCloneList)

print("The shuffled list is: ", operatingSystemCloneList)

print("The permutation list is: ", random.permutation(operatingSystemsList))

print("The original list is: ", operatingSystemsList)

# permutation returns new array and shuffle changes the original array
