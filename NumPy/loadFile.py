#This script shows how to demonestrate numpy loading files into arrays
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics


import numpy as np


serverData = np.loadtxt("NumPy/ServerData.csv", delimiter=",", dtype=str)

print(serverData)


###############

