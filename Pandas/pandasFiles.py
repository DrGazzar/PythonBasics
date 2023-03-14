#This script shows how to demonestrate pandas files
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics


import pandas as pd

serverData = pd.read_csv("Pandas/ServerData.csv")

print(serverData)

print(serverData.to_string())


##### system's maximum rows
print("System's maximum rows:  ",pd.options.display.max_rows)

## This maximum can be modified

pd.options.display.max_rows = 59

##########
#### Read json file using pandas

serverListFromJson = pd.read_json("Pandas/assets.json")

print("################# from JSON ##############")
print(serverListFromJson)



####### Python dictionaries are the same as JSON format

books = {

    "Python Crash Course" : {
        "Author": "Eric",
        "Topic" : "Python",
        "Pages" : 544 
        
    },

    "Automate with python" : {
        "Author": "Ed",
        "Topic" : "Automation",
        "Pages" : 200
        
    },
    
        "Learning python" : {
        "Author": "Mark",
        "Topic" : "Python",
        "Pages" : 600 
        
    }
    

}


allBooks = pd.DataFrame(books)

print("---------All books dictionary/json-----\n", allBooks)


######