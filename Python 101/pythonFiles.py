#This script shows how to demonestrate file handling in python
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics


######## reading a configuration file in to a list #############

conf = open ("Python 101/serverConfigurations.cnf", "r")


configurations =[]

for lines in conf:
    configurations.append(lines)

print(configurations)


conf.close()

####### writing in a file (append)############ 

conf = open ("Python 101/serverConfigurations.cnf", "a")

conf.write("Type= blade")

conf.close()  