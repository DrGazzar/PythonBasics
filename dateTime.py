#This script shows how to demonestrate the date time in python
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar) 
#Github repo: https://github.com/DrGazzar/PythonBasics

import datetime

print(datetime.datetime.now())  #date time

print(datetime.date.today())   #date only

print(datetime.datetime.now().year)  #year only

print(datetime.date.today().day)   #day only


####### creating date time for specific date


victoryDay = datetime.datetime(1973,10,6)

print(victoryDay.day)

print(victoryDay.year)
