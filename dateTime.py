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


vDay = datetime.datetime(1393,10,10)

print(vDay.day)

print(vDay.year)

#It is possible to format the date/time according to the format needed

print(vDay.strftime("%A - %w -  %m  -  %Y"))
