#This script shows how to demonestrate pandas data frames analysis
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics


import pandas as pd

serverData = pd.read_csv("Pandas/ServerData.csv")

print(serverData.head(1))

print(serverData.tail(1))
