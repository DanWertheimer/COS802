#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 13:37:18 2017

@author: danwertheimer
"""
import pandas as pd
from sklearn.utils import shuffle
from collections import defaultdict
from faker import Faker
import numpy as np
fake = Faker()
fake.seed(123)

# =============================================================================
# - Import all the data and sample 501 000 of the legitimate claims,
#   append the fake claims and add them to the dataset. Then shuffle
#   the dataset so there isn't any order.
# =============================================================================
LegitData = pd.read_csv("LegitData2.csv")
LegitData = LegitData.sample(n = 501000, random_state = 47)
FakeData = pd.read_csv("FraudData2.csv")

Data = LegitData.append(FakeData)

# - Drop the index column.
Data = Data.drop('Unnamed: 0', axis = 1)
BeforeAnonymisation = Data.head()

# Zip code anonymisation
Data['Policy_Holder_Postal_Code'] = Data['Policy_Holder_Postal_Code'].astype(str)
Data['Policy_Holder_Postal_Code'] = Data.apply(lambda x : \
    x['Policy_Holder_Postal_Code'][0:3] +'xx',axis = 1)
Data['Loss_Postal_Code'] = Data['Loss_Postal_Code'].astype(str)
Data['Loss_Postal_Code'] = Data.apply(lambda x : \
    x['Loss_Postal_Code'][0:3] +'xx',axis = 1)


# Hash Unique Identifier
Data['Client_ID'] = Data['Client_ID'].astype(str)
Data['Client_ID'] = Data['Client_ID'].apply(hash)

# - Replace names with fake names

# - Because names aren't important to machine learning algorithms
#   I choose to not care about the gender of the output name. It
#   shouldn't matter if someone knows the data is fake. It is
#   useless anyway.

FirstName = defaultdict(fake.first_name)
Surname = defaultdict(fake.last_name)
Test = Data.head()
FirstName[np.NaN] = None
Surname[np.NaN] = None

Data['Insured_First_Name'] = Data['Insured_First_Name'].map(FirstName)
Data['Insured_Last_Name'] = Data['Insured_Last_Name'].map(Surname)
Data['Other_Party_Name'] = Data['Other_Party_Name'].map(FirstName)
Data['Other_Party_Last_Name'] = Data['Other_Party_Last_Name'].map(Surname)

# Hash living locations
PersonalInformation = ['Policy_Holder_Street','Policy_Holder_State','Policy_Holder_City','Policy_Holder_Area']
Data[PersonalInformation] = Data[PersonalInformation].astype(str)
for i in PersonalInformation:
    Data[i] = Data[i].apply(hash)

LossInformation = ['Loss_Street','Loss_City','Loss_Area']
Data[LossInformation] = Data[LossInformation].astype(str)
for i in LossInformation:
    Data[i] = Data[i].apply(hash)

AfterAnonymisation = Data.head()
shuffle(Data).to_csv("FullyAnonymisedData2.csv")