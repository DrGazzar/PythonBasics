#This script shows how to demonestrate the user input (Hoe to receive input from the user)
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics


userName = input("Enter your username")

if userName == "":
    print("Username cannot be empty")
else:
    print("Your username is :  ", userName)

####### String formatting using format function

print ("--------------------")

outputMsg = "The formatted output is {} and it is entered by the user"

print(outputMsg.format(userName))