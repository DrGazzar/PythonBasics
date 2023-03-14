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
