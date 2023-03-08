#This script shows how to demonestrate dictionary in Python
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics


#Dictionary is used to store the data in key:value pairs

serverData = {
"server type" : "web",
"software" : "apache",
"deployment date" : 23,
"deployment month" : 12,
"deployment year" : 2022
}

print(serverData)

print(serverData["server type"])

# Change items on the dictionary

serverData["deployment year"] = 2023
print(serverData)


# Add items to the dictionary

serverData["deployment path"] = "/opt"
print(serverData)


# remove items from the dictionary

serverData.pop("deployment path")
print(serverData)
