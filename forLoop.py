#This script shows how to demonestrate the for loop
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics

#loop the letters in a string - mind the indentation

for letter in "Welcome to Python":
    print (letter)


#loop the items in a list

courses = ["OS", "Networks", "Programming Languages 1", "Data Structures" , "Algorithms"]
for courseName in courses:
    print ("The course name is --> ", courseName)


# combining for statement and if statement

for courseName in courses:
    if courseName == "Algorithms":
        print ("The course name is --> ", courseName)


# continue statement to skip the current iteration

for courseName in courses:
    if courseName == "Algorithms":
        continue
    print ("The course name is --> ", courseName)
