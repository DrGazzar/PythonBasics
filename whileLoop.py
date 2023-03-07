#This script shows how to demonestrate the for loop
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics

numberOfRequests = 10

while numberOfRequests > 0:
    print('The current number of requests is :  ', numberOfRequests)
    numberOfRequests -= 1


#break statement is used to abort the while loop even if the condition is still evaluated to true
numberOfRequests = 10

while numberOfRequests > 0:
    print('The current number of requests is :  ', numberOfRequests)
    if numberOfRequests == 5:
        break
    numberOfRequests -= 1
