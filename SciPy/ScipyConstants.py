#This script shows how to demonestrate scipy constants
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics

from scipy import constants
from scipy import optimize
import numpy as np

########### constants

print(constants.liter)

print("PI ", constants.pi)

print("The available list of modules ", dir(constants))

print("gram ", constants.gram)

####### optimizing functions

####### roots of linear equations (cannot get the roots of non linear equations)

def equat (x):
    return x + np.sqrt(25)

myroot = optimize.root(equat, 4)

print("The root is ", myroot)