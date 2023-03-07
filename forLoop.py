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



# loop on a range of numbers from the starting argument to the number before the last argument
# default increment 1 is used

for countingNumbers in range (1,10):
    print(countingNumbers)

# loop on a range of numbers from the starting argument to the number before the last argument
# increment by 1 is used

print ("skip counting by 2")
for countingNumbers in range (1,10,2):
    print(countingNumbers)

# for loop can be nested

for countingNumbers in range (1,10,2):
    for specificCounts in range(countingNumbers, 10):
        print('Inner loop and the value of specificCounts is --> ', specificCounts) 
        #Note it will display the numbers each time starting from the new value of countingNumbers 
    print ("---------------------------- An iteration of the outer loop ------------")    


