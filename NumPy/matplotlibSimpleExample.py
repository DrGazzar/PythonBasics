#This script shows how to demonestrate numpy matplotlib
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics


## Work in progress 


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#### an example using the tips build-in data set


tipsData = sns.load_dataset("tips")

tipsData.head()

sns.displot(data=tipsData, x="total_bill")

plt.show()

##################

