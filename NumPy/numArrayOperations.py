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
