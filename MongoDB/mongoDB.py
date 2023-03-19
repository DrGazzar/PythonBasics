#This script shows how to connect to MongoDB
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics


import pymongo

clientDB = pymongo.MongoClient("mongodb://localhost:27017/")

workingDB = clientDB["workingDB"] 

#### MongoDB does not create the database untill there are some contents inside it
#### collection includes documents 
#### Documents are similar to - but not exactly the same as - rows
#### Documents have to have key value pairs
#### e.g.  {username: 'a name', address: 'an address'}  --> looks like the python dictionary and JSON files

### creating collection
### collection is not created until there are some contents in it

workingCollection = workingDB["serverLogs"]

### to insert a dictionary , we could create a dictionary

serverData = {
    "serverName" : "web server",
    "serverSoftware" : "Apache Web Server",
    "Proxy" : "Yes"
}

insertionData = workingCollection.insert_one(serverData)

print("The ID of the inserted data is: ",insertionData.inserted_id)

### can insert multiple documents at one statement ... using list of dictionaries

allServers = [
{"serverName" : "Database Server", "serverSoftware": "MongoDB", "Proxy": "N/A"},
{"serverName" : "Structured Database 1", "serverSoftware": "MySql", "Proxy": "N/A"},
{"serverName" : "Structured Database 2", "serverSoftware": "Oracle", "Proxy": "N/A"},
{"serverName" : "Print Server", "serverSoftware": "Samba", "Proxy": "No"},
{"serverName" : "Mail Server", "serverSoftware": "qmail", "Proxy": "No"}

]

insertionMultipleDocuments = workingCollection.insert_many(allServers)

print("The ID of the inserted documents is: ",insertionMultipleDocuments.inserted_ids)


########################################################################
### check if a database exists

listOfDatabases = clientDB.list_database_names()
listOfCollections = workingDB.list_collection_names()

print ("List of Databases :", listOfDatabases)
print ("List of collections :", listOfCollections)


if "serverLogs" in listOfCollections:
    print("----------- Collection exists -----------")

################################
### select data from the collection

#for selectedDocument in workingCollection.find():
#    print("The selected document is : ", selectedDocument)

for selectedDoc in workingCollection.find( { "serverName":"Database Server", "serverSoftware":"MongoDB" }):
    print("returned documents: ",selectedDoc)


####### Selection using query object (filtering the result) ##########

searchFor = {"serverName": "web server"}

resultSet = workingCollection.find(searchFor)

print ("######################################################")

for oneItem in resultSet:
    print ("result record ", oneItem)


