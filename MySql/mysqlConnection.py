#This script shows how to demonestrate mysql db connecion
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics

import mysql.connector

######### database connection

dbConnection = mysql.connector.connect (
    host="localhost",
    user="root",
    password="---------"

)

##### databse creation
myStatement = dbConnection.cursor()

#myStatement.execute("create database sampleDB")

myStatement.execute("show databases")

for eachRow in myStatement:
    print(eachRow)



#### connecting to the created DB

newDbConnection = mysql.connector.connect (
    host="localhost",
    user="root",
    password="--------",
    database="sampleDB"
)

print(newDbConnection)

newMyStatement = newDbConnection.cursor()


###### creating table

#newMyStatement.execute('create table servers (id int,name varchar(200), software varchar(200) )  ')

newMyStatement.execute("show tables")

for myRow in newMyStatement:
    print(myRow)

######## inserting data

newMyStatement.execute('insert into servers values (1, \'web server\' , \'apache we server\' )')


###### selecting

newMyStatement.execute('select * from servers')

result = newMyStatement.fetchall()

for newReturnedRow in result:
    print(newReturnedRow)

