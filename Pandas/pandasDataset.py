#This script shows how to demonestrate numpy loading files into arrays
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics


import pandas as pd

students = {

'course_name': ["Operating Systems","Programming Language 1","Networks"],
'No of students': [30,50,20],
'No of teachers': [2,5,3]

}


studentsCount = pd.DataFrame(students)

print(studentsCount)



###### checking pandas version

print("------------------")
print("The current pandas version is ...   ",pd.__version__)


############# Series (similar to one dimensional array)


courseNames = ["Operating Systems", "Networks", "Introduction to Computers"]

coursesSeries = pd.Series(courseNames)

print ("-------------------#####--------------")
print(coursesSeries)


############### labels ##############
#### default is the index
print(coursesSeries[2])


##### but it is possible to specify our own label

coursesSeries_2 = pd.Series(courseNames,  index = ["First_Course","Second_Course","Third_Course"])

print("Printing by label: ",coursesSeries_2['First_Course'])


######### from dictionary

coursesDict = {
"Programming Languages" : 20,
"Networks" : 60,
"Introduction to Computers" : 30,
"Introduction to Linear Algebra" : 80
} 

coursesFromDict = pd.Series(coursesDict)

print("###############################")
print(coursesFromDict)


######## Dataframes like 2-D data structure or table with rows and columns

studentsDataset = pd.DataFrame(students )
studentsDataset2 = pd.DataFrame(students, index = ["Course 1", "Course 2","Course 3"])
print("###############################")
print(studentsDataset)


##### return one or more rows using loc

print("One row \n ####################\n", studentsDataset.loc[1:1])

print("By label  \n ####################\n", studentsDataset2.loc["Course 1"])

##########

