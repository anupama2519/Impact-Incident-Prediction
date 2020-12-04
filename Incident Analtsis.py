# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 12:03:09 2020

@author: admin
"""

#Load the required libraries:

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split 


#Read the dataset:
    
incident_anal = pd.read_excel('C:/Users/admin/Desktop/python program files/Project/project 2/Incidents_service.xlsx')

incident_anal.head()


#Exploratory Data Analysis


#To know the data :
print(incident_anal.info())

# 3 Dates,  3 integers, 3 boolean values, 16 categorical values

#Check for null values:
    
incident_anal.isnull().sum()   # No missing values

#summary of numerical values:
summary_num = incident_anal.describe()
print(summary_num)


#summary of categorical values:
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)
summary_cat = incident_anal.describe(include = 'O')
print(summary_cat)



# There are some undefined characters/symbols in dataset:
#Read the dataset again without special character ?

incident_new = pd.read_excel('C:/Users/admin/Desktop/python program files/Project/project 2/Incidents_service.xlsx',na_values=['?'])
                        
incident_new.isnull().sum()

#treat the missing values:
missing = incident_new[incident_new.isnull().any(axis=1)]
incident_new  = incident_new.dropna(axis=0)
