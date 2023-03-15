#This script shows how to demonestrate pandas cleaning data
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics


import pandas as pd

serverData = pd.read_csv("Pandas/ServerRawData.csv")


######## drop the rows that had empty values ########
newServerData = serverData.dropna()

print(newServerData)


####### replace empty values ###########

replacedServerData = serverData.fillna("NO VALUE HERE")

print("#################################")
print(replacedServerData)


######## replace empty for specific columns - will return only the column ###########

replacedSpecific = serverData["server_storage"].fillna("NO STORAGE specified here")

print("#################################")
print(replacedSpecific)

################### Calculate mean ################

serverStorageAverage = newServerData["server_storage"].mean()

print("\n\n\n###################____ calculate mean _______ #############")
print("Mean value is: ",serverStorageAverage)

###################################
