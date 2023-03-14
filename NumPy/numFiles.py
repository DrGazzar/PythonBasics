#This script shows how to demonestrate numpy I/O
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics


import numpy as np


serverData = np.loadtxt("NumPy/ServerData.csv", delimiter=",", dtype=str)

print(serverData)

print("The data types is: ",type(serverData))


serverData[1,1] = "Apache"

serverSubsetData = serverData[1:5, 1:5]

print(serverSubsetData)

np.savetxt('NumPy/ServerData_Modified.csv', serverSubsetData ,delimiter=',', fmt='%s')

##################

