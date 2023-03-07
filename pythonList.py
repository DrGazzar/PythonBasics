#This script shows how to demonestrate lists in Python
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics

courses = ['OS', 'Programming Language', 'Math1', 'Algorithms']

print(courses)

# Lists allow duplicate values

programmingLanguages = ['Python', 'Java', 'C', 'Python']

print(programmingLanguages)

# Lists allows different Data Types

programLang = ['Python',1,'Java', 2, 'C', 3.1]

print (programLang)

# Lists are changeable - 0 based indexing

programLang[2] = 'Java Programming Language'

print (programLang)

# Add item to the list

programLang.append('C++') # add the end of the list
programLang.insert(4, 'Php') # add at specified index

print (programLang)

# remove item from the list

programLang.remove('Php') #remove specific item
programLang.pop(4)  #remove item at specified index
print (programLang)

del programmingLanguages # remove the entire list
programLang.clear() #empty the list

print(programLang) # will display empty list
# 