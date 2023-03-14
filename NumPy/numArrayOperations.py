#This script shows how to demonestrate some numpy array operations like joining
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics


import numpy as np


###### concatenate by axis 0
csCourse1stGrade = np.array(['OS','Networks','Digital Design'])
csCourse2ndGrade = np.array(['Java','C++','Python'])

computerScienceCourses = np.concatenate((csCourse1stGrade,csCourse2ndGrade))

print("Computer Science Courses are: ", computerScienceCourses)

#######

infrastructureSeversNo1 = np.array([['web server', 'application server'], ['DB server','file server']])
infrastructureSeversNo2 = np.array([['mail server', 'ftp server'], ['file server','print server']])

infrastructureFullList = np.concatenate((infrastructureSeversNo1, infrastructureSeversNo2), axis=1)

print("the infrastructure full list is: \n",infrastructureFullList)


print("staking", np.stack((infrastructureSeversNo1, infrastructureSeversNo2), axis=1))


########### Splitting arrays ############

infrastructurePartialList = np.array_split(infrastructureSeversNo1,2)

print("The partial list is: ", infrastructurePartialList)


########### Array search using where

programmingLang = np.where (computerScienceCourses=="Java")

print(programmingLang)

############# array sort ###########

sortedComputerScienceCourse = np.sort(computerScienceCourses)

print("sorted", sortedComputerScienceCourse)


######## creating uninitialized array

lectures = np.empty([5,3], dtype=int)

print("The empty array (filled with random values) is: ",lectures )

####### return an array filled of zeros

zeros = np.zeros([4,5], dtype=float)

print("the zeros array is: ", zeros)

####### Not only filled with zeros, it can be filled with ones too ######

ones = np.ones([2,4], dtype=int)

print("The array filled with ones is: ", ones)

######## convert a buffer (e.g. string) to a numpy array
##### The letter b before string to convert it to byte format 
programmingLanguageName = b'Python Programming Language'

separatedProg = np.frombuffer(programmingLanguageName, dtype = 'S1')

print("The separated name is: ", separatedProg)

print(separatedProg[8].decode('UTF-8'))

##### The above line is to decode to UTF-8

