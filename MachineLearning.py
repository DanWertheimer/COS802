#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 17:23:39 2017

@author: danwertheimer
"""
1209/10000

import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import Normalizer
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.pipeline import Pipeline
Data = pd.read_csv("CleanData2.csv",index_col = 0)
Fields =['Insured_First_Name','Insured_Last_Name','Client_ID','Other_Party_Name',\
                'Other_Party_Last_Name','Fraudulent_Claim_Reason',\
                'Policy_Holder_Street',\
                'Policy_Holder_State',\
                'Policy_Holder_City',\
                'Policy_Holder_Area',\
                'Policy_Holder_Postal_Code',\
                'Loss_Street',\
                'Loss_State',\
                'Loss_City',\
                'Loss_Area',\
                'Loss_Postal_Code']
Data = Data.drop(Fields,axis = 1)

ScaledVariables = ['Amount_Paid','Sum_Insured','Total_Policies_Revenue']
mms = preprocessing.MinMaxScaler()
Normalize = preprocessing.Normalizer()
Data[ScaledVariables] = Normalize.fit_transform(Data[ScaledVariables])
Test1 = Data[Data['Fraudulent_Claim_Indicator'] == 0].sample(n = 10000 )
Test2 = Data[Data['Fraudulent_Claim_Indicator'] == 1]
New = pd.concat([Test1,Test2], axis = 0)
DataX = New[New.columns.difference(['Fraudulent_Claim_Indicator','Date_Of_Birth',\
                                      'Date_Of_Loss','Policy_Start_Date',\
                                      'Policy_End_Date'])]
DataY = New['Fraudulent_Claim_Indicator']
X_train, X_test, y_train, y_test = train_test_split(\
                DataX, DataY, test_size=0.8, random_state=48)

glm = LogisticRegression()
glm.fit(X_train,y_train)
glm.score(X_test,y_test)
glmcv = cross_val_score(glm, DataX, DataY, cv=10,scoring = 'roc_auc')
clf = svm.SVC(kernel='linear', C=2).fit(X_train, y_train)
clf.score(X_test, y_test) 
clfcv = cross_val_score(clf, DataX, DataY, cv=10,scoring = 'roc_auc')
NNet = MLPClassifier(solver='lbfgs', alpha=1e-5,\
                    hidden_layer_sizes=(3, 2), random_state=47)
NNet.fit(X_train,y_train);
NNet.score(X_test, y_test) 
NNetcv = cross_val_score(NNet, DataX, DataY, cv=10,scoring = 'roc_auc')
###############################################################################
FeatureData = Data
DateFeatures = ['Date_Of_Birth','Date_Of_Loss','Policy_Start_Date',\
                    'Policy_End_Date']
FeatureData[DateFeatures] = FeatureData[DateFeatures].astype(str)
for i in DateFeatures:
    FeatureData[i] = pd.to_datetime(FeatureData[i])
# Creating feature for days between policy start and loss
FeatureData['Days_Between_Policy_Loss'] = FeatureData['Date_Of_Loss'] - FeatureData['Policy_Start_Date']
FeatureData['Days_Between_Policy_Loss'] = FeatureData['Days_Between_Policy_Loss'].apply(lambda x:x.days)   
# Creating feature for days between policy loss and policy end
FeatureData['Days_Before_Policy_End_Loss'] = FeatureData['Policy_End_Date'] - FeatureData['Date_Of_Loss'] 
FeatureData['Days_Before_Policy_End_Loss'] = FeatureData['Days_Before_Policy_End_Loss'].apply(lambda x:x.days)   

FeatureData['Number_Of_Claims'] = FeatureData.groupby(['Date_Of_Birth','Policy_Start_Date',\
                    'Policy_End_Date']).cumcount()+1
# Rescaling New Features
NewFeatures = ['Days_Between_Policy_Loss','Days_Before_Policy_End_Loss','Number_Of_Claims']
FeatureData[NewFeatures] = Normalize.fit_transform(FeatureData[NewFeatures])



###############################################################################
# Retraining Models
Test1 = FeatureData[FeatureData['Fraudulent_Claim_Indicator'] == 0].sample(n = 10000 )
Test2 = FeatureData[FeatureData['Fraudulent_Claim_Indicator'] == 1]
NewFeatureData = pd.concat([Test1,Test2], axis = 0)
DataX = NewFeatureData[NewFeatureData.columns.difference(['Fraudulent_Claim_Indicator','Date_Of_Birth',\
                                      'Date_Of_Loss','Policy_Start_Date',\
                                      'Policy_End_Date'])]
DataY = NewFeatureData['Fraudulent_Claim_Indicator']
# Checking Variable Importance
Tree = ExtraTreesClassifier()
TreeC = Tree.fit(DataX,DataY)
TreeC.feature_importances_  
model = SelectFromModel(TreeC, prefit=True)
X_new = model.transform(DataX)

X_train_newfeature, X_test_newfeature, y_train_newfeature, y_test_newfeature = train_test_split(\
                X_new, DataY, test_size=0.8, random_state=48)

glm_newfeature = LogisticRegression()
glm_newfeature.fit(X_train_newfeature,y_train_newfeature)
glm_newfeature.score(X_test_newfeature,y_test_newfeature)

glmcv2 = cross_val_score(glm_newfeature, X_new, DataY, cv=10, scoring = 'roc_auc')

clf_newfeature = svm.SVC(kernel='linear', C=1).fit(X_train_newfeature, y_train_newfeature)
clf_newfeature.score(X_test_newfeature, y_test_newfeature) 
clfcv2 = cross_val_score(clf_newfeature, X_new, DataY, cv=10, scoring = 'roc_auc')

NNet_newfeature = MLPClassifier(solver='lbfgs', alpha=1e-5,\
                    hidden_layer_sizes=(3, 2), random_state=47)
NNet_newfeature.fit(X_train_newfeature,y_train_newfeature);
NNet_newfeature.score(X_test_newfeature, y_test_newfeature) 
NNetcv2 = cross_val_score(NNet_newfeature, X_new, DataY, cv=10, scoring = 'roc_auc')

Q = Pipeline([
  ('feature_selection', SelectFromModel(LinearSVC())),
  ('classification', RandomForestClassifier())
])

Q.fit(X_train_newfeature,y_train_newfeature)

Q.score(X_test_newfeature, y_test_newfeature) 
