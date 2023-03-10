#This script shows how to demonestrate numpy arrays
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics

import numpy as np #you can make alias for the library


### Defining an array in Python
serverList = np.array(["web server", "email server", "database server"])

print(serverList)

print("The type of numpy array is: ", type(serverList))

###### numpy has different versions
## Version can be checked by

print(np.__version__)

####################

###### Actually, the numpy array can have sny type of python array like objects like list or tuples

operatingSystems = ("Linux", "macOS", "Windows", "Unix")

npOperatingSystems = np.array(operatingSystems)

print(type(npOperatingSystems))
print(npOperatingSystems)


##########################
#Multi-Dimensional arrays

programmingLang = np.array([["C","C++"],["Java", "C#"],["PHP", "JavaScript"]])

print(programmingLang)

print("The number of dimensions of the numpy array is ",programmingLang.ndim)


#### Access array element

print(programmingLang[0,1])
print(programmingLang[2,1])


#A nice trick to use is the negative indexing (access from the rear)

print(programmingLang[0,-1])

#You can also slice the elements

commonWebLanguages = programmingLang[1:]

print("Languages that could be used in building web sites: ",commonWebLanguages)

###################

#You can use steps in slicing
#First item is the starting index, second is the ending index and the third is the step 
#In the below example starting index 0, ending index is not specified which means the end of the array
#the step is 2

subsetProgramming = programmingLang[0::2]

print("Subset of the programming languages: ",subsetProgramming)

