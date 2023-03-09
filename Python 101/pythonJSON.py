#This script shows how to demonestrate JSON processing in Python
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics

import json

#### Converting from Python dictionary to JSON

serverConfiguration = {   #Dictionary
    "processor" : "x86",
    "storage" : "SSD",
    "storageSize" : "512",
    "memorySize" : "16",
    "software": [
        {"OS": "macOS", "version":"12"},
        {"ProgrammingLanguage" : "Python", "version" : "3.10"}
    ]
}

serverConfigurationJSON = json.dumps(serverConfiguration)

print(serverConfigurationJSON)



########## using indentation to format the printing

serverConfigurationJSONIndentation = json.dumps(serverConfiguration, indent=4)
print("-------------\n",serverConfigurationJSONIndentation)
