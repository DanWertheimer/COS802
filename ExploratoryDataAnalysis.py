#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 14:42:55 2017

@author: danwertheimer
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
'''
def LossCategory(A):
    if A =='Wind and Hail':
        return 1
    elif A =='Water Damage':
        return 2
    elif A == 'Fire':
        return 3
    elif A == 'Theft':
        return 4
    elif A == 'Malicious Damage':
        return 5
    elif A == 'Subsidence':
        return 6
    elif A == 'Other Property Damage':
        return 7
def MaritalStatusCategory(A):
    if A == 'Married':
        return 1
    elif A == 'Widow':
        return 2
    elif A == 'Single':
        return 3
    elif A == 'Divorced':
        return 4
def LossItemCategory(A):
    if A == 'House':
        return 1
    elif A == 'Electronics':
        return 2
    elif A == 'Jewllery':
        return 3
    elif A == 'Less than 5 Items':
        return 4
    elif A =='More than 5 Items':
        return 5
    elif A == 'Antiques':
        return 6
    elif A == 'Miscellanious':
        return 7
'''
Data = pd.read_csv("FullyAnonymisedData2.csv",index_col = 0)

Data.describe()
Data.info()
A = Data[pd.isnull(Data) == True]

# Checking that there are no fraudulent claims without a reason.
Data.loc[(Data['Fraudulent_Claim_Reason'] == np.nan) & (Data['Fraudulent_Claim_Indicator']==1)]
Data.loc[Data['Amount_Paid']<0]

plt.figure(figsize=(9, 8))
sns.distplot(Data['Sum_Insured'], color='g', bins=100, hist_kws={'alpha': 0.4});
sns.distplot(Data['Amount_Paid'], color='g', bins=50, hist_kws={'alpha': 0.4});

list(set(Data.dtypes.tolist()))
NumericalData = Data.select_dtypes(include = ['float64', 'int64'])
AnonymisedData = ['Client_ID' ,'Policy_Holder_Street','Policy_Holder_State',\
                  'Policy_Holder_City','Policy_Holder_Area','Loss_Street',\
                  'Loss_City','Loss_Area']
NumericalData = NumericalData.drop(AnonymisedData, axis = 1)
NumericalData.head()
NumericalData.hist(figsize=(9, 8), bins=50, xlabelsize=8, ylabelsize=8)

Data.boxplot(column = ["Amount_Paid"],
                      by = "Kind_Of_Loss",
                      figsize = (8,8))
plt.xticks(rotation=45)
plt.texts()
# Cleaning Data Types
UsefulData = Data
UsefulData.dtypes
UsefulData.Broker_ID = UsefulData.Broker_ID.astype(object)
# Creating categorical variables
UsefulData = pd.concat([UsefulData.drop('Marital_Status', axis=1),\
                        pd.get_dummies(UsefulData['Marital_Status'])], axis=1)
UsefulData = UsefulData.drop('Widow', axis = 1)

UsefulData = pd.concat([UsefulData.drop('Gender', axis=1),\
                        pd.get_dummies(UsefulData['Gender'],prefix = 'is')],\
                        axis=1)
UsefulData = UsefulData.drop('is_F', axis = 1)

UsefulData = pd.concat([UsefulData.drop('Kind_Of_Loss', axis=1),\
                        pd.get_dummies(UsefulData['Kind_Of_Loss'])],\
                        axis=1)
UsefulData = UsefulData.drop('Water Damage', axis = 1)

UsefulData = pd.concat([UsefulData.drop('Loss_Item', axis=1),\
                        pd.get_dummies(UsefulData['Loss_Item'])],\
                        axis=1)
UsefulData = UsefulData.drop('Miscellanious', axis = 1)

UsefulData = pd.concat([UsefulData.drop('Claim_Service_Provider', axis=1),\
                        pd.get_dummies(UsefulData['Claim_Service_Provider'])],\
                        axis=1)
UsefulData = UsefulData.drop('Wilson-Perez', axis = 1)
UsefulData = UsefulData.drop('Broker_ID', axis = 1)
UsefulData.to_csv("CleanData2.csv")