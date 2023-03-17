#This script shows how to demonestrate pandas cleaning data
#License GPL
#Created by: Mohamed ElGazzar (DrGazzar)
#Github repo: https://github.com/DrGazzar/PythonBasics

import pandas as pd


######## fixing format (e.g. date format)
deploymentData = pd.read_csv('Pandas/DeploymentData.csv')

deploymentData['deployment_date']= pd.to_datetime(deploymentData['deployment_date'])

print("The deployment data is: \n\n", deploymentData.to_string())


######  removing duplicates

deploymentData.drop_duplicates(inplace=True)

print("The deployment data after removing the duplicates is: \n\n", deploymentData.to_string())