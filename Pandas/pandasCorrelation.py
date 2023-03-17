#This script shows how to demonestrate pandas correlation between columns
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics

import pandas as pd
import matplotlib.pyplot as plt


studentResults = pd.read_csv('Pandas/studentResults.csv')
print(studentResults.corr())


studentResults.plot()

plt.show()