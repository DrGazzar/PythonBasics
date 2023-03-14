#This script shows how to demonestrate numpy matrix
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics


#Matrix is strictly 2 dimensional array and inherits ndarray

import numpy.matlib
import numpy as np

devices = np.matlib.empty([3,4], dtype="str")

print(devices)

initialDeviceList = np.matlib.zeros([5,6], dtype="int")

print(initialDeviceList)


oneInEveryOne = np.matlib.ones([3,9])

print(oneInEveryOne)

####### ones in the diagonal ##### note the case of n , M, k

diagonalList = np.matlib.eye(n=9, M=9, k=0, dtype="int")

print(diagonalList)

