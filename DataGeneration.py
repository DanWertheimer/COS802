#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 08:45:54 2017

@author: danwertheimer
"""
from faker import Faker
import pandas as pd
import random
import numpy as np
import datetime as dt
from random import choice
from faker.providers import BaseProvider


# =============================================================================
#        Creating Random Providers
# =============================================================================
class ExtrasProvider(BaseProvider):
    @classmethod
    def marital(self):
        return choice([
        'Single', 'Single', 'Single','Single', 'Married', 'Widow', 'Divorced', 'Married', 'Married', 'Married'
    ]
)
    def company2(self):
        return choice([
                'Baker, Griffith and Moses','Moore LLC','Steele PLC','Lewis, Johnson and Hill','Wilson-Perez'
                ])
    def loss(self):
        return choice([
                'Wind and Hail','Water Damage','Fire','Theft','Theft','Theft','Theft','Malicious Damage','Subsidence', 'Other Property Damage'
                ])
    def Area(self):
        areas = pd.read_csv('us-cities-sample.csv')
        areas = areas.name.tolist()
        return choice(areas)
    def Item(self):
        return choice([
                'House','Electronics','Jewllery','Less than 5 Items','More than 5 Items','Antiques','Miscellanious'
                ])
    def NoOfClaims(self):
        return choice([
                1,1,1,1,1,2,2,3
                ])
    def FakeNoOfClaims(self):
        return choice([
                3,3,4,4,5,6,7,8
                ])
    def CompanyID(self,company):
        if company == 'Baker, Griffith and Moses':
            return 1
        elif company == 'Moore LLC':
            return 2
        elif company == 'Steele PLC':
            return 3
        elif company == 'Lewis, Johnson and Hill':
            return 4
        else:
            return 5
# =============================================================================
#       Initialisation
# =============================================================================
fake = Faker()
fake.add_provider(ExtrasProvider)
fake.seed(47)
random.seed(50)
MalePercent = random.uniform(0.4,0.6)
FemalePercent = 1 - MalePercent
content = []

# =============================================================================
# Creation of legitimate claims
# =============================================================================
# Males
def GenerateMale(Percent):
    content = []
    for i in range(0,round(450000 * Percent)):
        FirstName = fake.first_name_male()
        Surname = fake.last_name_male()
        ClientID = int(''.join(random.sample('123456789',6)))
        DOB = fake.date_between(start_date="-90y", end_date="-20y");
        Date_of_loss = fake.date_between(start_date = DOB + dt.timedelta(days=365*18), end_date="-1d");
        Policy_Start = fake.date_between(start_date = DOB + dt.timedelta(days=365*17), end_date = Date_of_loss);
        Policy_End = fake.date_between(start_date = Policy_Start + dt.timedelta(days=30), end_date = Date_of_loss+ dt.timedelta(days=21900));
        Time_On_Policy = round((Date_of_loss - Policy_Start).days/30)+1
        Monthly_Cost = round(float(np.random.normal(1083,300,1))/12,2)
        Total_Policy_Revenue = round(Time_On_Policy*Monthly_Cost,2)
        Sum_Insured = Total_Policy_Revenue*random.uniform(1,1.3)
        Street_Address = fake.street_address()
        State = fake.state()
        City = fake.city()
        Postal_Code = fake.postalcode()
        Area = fake.Area()
        Company = fake.company2()
        Company_ID = fake.CompanyID(Company)
        for i in range(0,fake.NoOfClaims()):
            
    
            if random.random() > 0.99:
                Other_Party_Name = fake.first_name()
                Other_Party_Last_Name = fake.last_name()
                Kind_Of_Loss = 'Malicious Damage'
            else:
                Other_Party_Name = None
                Other_Party_Last_Name = None
                Kind_Of_Loss = fake.loss()
    
            if Kind_Of_Loss != 'Theft':
                Item = 'House'
                Amount_Paid = round(random.uniform(60000,200000),2)
            else:
                Item = fake.Item()
                if Item in ['Electronics','Jewllery','More than 5 Items','Antiques']:
                    Amount_Paid = round(random.uniform(50,800),2)
                else:
                    Amount_Paid = round(random.uniform(30,200),2)
    
    
    
    
            if random.random() > 0.2:
                Loss_Street_Address = Street_Address
                Loss_State = State
                Loss_City = City
                Loss_Postal_Code = Postal_Code
                Loss_Area = Area
            else:
                Loss_Street_Address = fake.street_address()
                Loss_State = fake.state()
                Loss_City = fake.city()
                Loss_Postal_Code = fake.postalcode()
                Loss_Area = fake.Area()
    
    
            info = {
            'Insured_First_Name' : FirstName,
            'Insured_Last_Name' : Surname,
            'Client_ID' : ClientID,
            'Gender' : 'M',
            'Date_Of_Birth' : DOB,
            'Marital_Status' : fake.marital(),
            'Policy_Holder_Street' : Street_Address,
            'Policy_Holder_State' : State,
            'Policy_Holder_City' : City,
            'Policy_Holder_Area' : Area,
            'Policy_Holder_Postal_Code' : Postal_Code ,
            'Loss_Street' : Loss_Street_Address,
            'Loss_State' : Loss_State,
            'Loss_City' : Loss_City,
            'Loss_Area' : Loss_Area,
            'Loss_Postal_Code' : Loss_Postal_Code ,
            'Loss_Item' : Item,
            'Sum_Insured' : Sum_Insured,
            'Total_Policies_Revenue' : Total_Policy_Revenue,
            'Kind_Of_Loss' : Kind_Of_Loss,
            'Amount_Paid' : Amount_Paid,
            'Policy_Start_Date' : Policy_Start,
            'Policy_End_Date' : Policy_End,
            'Other_Party_Name' : Other_Party_Name,
            'Other_Party_Last_Name' : Other_Party_Last_Name,
            'Claim_Service_Provider': Company,
            'Broker_ID' : Company_ID,
            'Date_Of_Loss' : Date_of_loss ,
            'Fraudulent_Claim_Indicator' : 0,
            'Fraudulent_Claim_Reason' : None
            }
            content.append(info)
    return(content)

# Females
def GenerateFemale(Percent):
    content = []
    for i in range(0,round(450000 * Percent)):
        FirstName = fake.first_name_female()
        Surname = fake.last_name_female()
        ClientID = int(''.join(random.sample('123456789',6)))
        DOB = fake.date_between(start_date="-90y", end_date="-20y");
        Date_of_loss = fake.date_between(start_date = DOB + dt.timedelta(days=365*18), end_date="-1d");
        Policy_Start = fake.date_between(start_date = DOB + dt.timedelta(days=365*17), end_date = Date_of_loss);
        Policy_End = fake.date_between(start_date = Policy_Start + dt.timedelta(days=30), end_date = Date_of_loss+ dt.timedelta(days=21900));
        Time_On_Policy = round((Date_of_loss - Policy_Start).days/30)+1
        Monthly_Cost = round(float(np.random.normal(1083,300,1))/12,2)
        Total_Policy_Revenue = round(Time_On_Policy*Monthly_Cost,2)
        Sum_Insured = Total_Policy_Revenue*random.uniform(1,1.3)
        Street_Address = fake.street_address()
        State = fake.state()
        City = fake.city()
        Postal_Code = fake.postalcode()
        Area = fake.Area()
        Company = fake.company2()
        Company_ID = fake.CompanyID(Company)
        for i in range(0,fake.NoOfClaims()):
            
    
            if random.random() > 0.99:
                Other_Party_Name = fake.first_name()
                Other_Party_Last_Name = fake.last_name()
                Kind_Of_Loss = 'Malicious Damage'
            else:
                Other_Party_Name = None
                Other_Party_Last_Name = None
                Kind_Of_Loss = fake.loss()
    
            if Kind_Of_Loss != 'Theft':
                Item = 'House'
                Amount_Paid = round(random.uniform(60000,200000),2)
            else:
                Item = fake.Item()
                if Item in ['Electronics','Jewllery','More than 5 Items','Antiques']:
                    Amount_Paid = round(random.uniform(50,800),2)
                else:
                    Amount_Paid = round(random.uniform(30,200),2)
    
    
    
    
            if random.random() > 0.2:
                Loss_Street_Address = Street_Address
                Loss_State = State
                Loss_City = City
                Loss_Postal_Code = Postal_Code
                Loss_Area = Area
            else:
                Loss_Street_Address = fake.street_address()
                Loss_State = fake.state()
                Loss_City = fake.city()
                Loss_Postal_Code = fake.postalcode()
                Loss_Area = fake.Area()
    
    
            info = {
            'Insured_First_Name' : FirstName,
            'Insured_Last_Name' : Surname,
            'Client_ID' : ClientID,
            'Gender' : 'F',
            'Date_Of_Birth' : DOB,
            'Marital_Status' : fake.marital(),
            'Policy_Holder_Street' : Street_Address,
            'Policy_Holder_State' : State,
            'Policy_Holder_City' : City,
            'Policy_Holder_Area' : Area,
            'Policy_Holder_Postal_Code' : Postal_Code ,
            'Loss_Street' : Loss_Street_Address,
            'Loss_State' : Loss_State,
            'Loss_City' : Loss_City,
            'Loss_Area' : Loss_Area,
            'Loss_Postal_Code' : Loss_Postal_Code ,
            'Loss_Item' : Item,
            'Sum_Insured' : Sum_Insured,
            'Total_Policies_Revenue' : Total_Policy_Revenue,
            'Kind_Of_Loss' : Kind_Of_Loss,
            'Amount_Paid' : Amount_Paid,
            'Policy_Start_Date' : Policy_Start,
            'Policy_End_Date' : Policy_End,
            'Other_Party_Name' : Other_Party_Name,
            'Other_Party_Last_Name' : Other_Party_Last_Name,
            'Claim_Service_Provider': Company,
            'Broker_ID' : Company_ID,
            'Date_Of_Loss' : Date_of_loss ,
            'Fraudulent_Claim_Indicator' : 0,
            'Fraudulent_Claim_Reason' : None
            }
            content.append(info)
    return(content)
###############################################################################
# Case When Large Amount Claimed Shortly After Policy Start
def GenerateFakeFemale1(Percent):
    content = []
    for i in range(0,round(500 * Percent)):
        ClientID = int(''.join(random.sample('123456789',6)))
        DOB = fake.date_between(start_date="-90y", end_date="-20y");
        Policy_Start = fake.date_between(start_date = DOB + dt.timedelta(days=365*18), end_date = "-1d");
        Date_of_loss = fake.date_between(start_date = Policy_Start + dt.timedelta(days=1), end_date=Policy_Start + dt.timedelta(days=45));
        Policy_End = fake.date_between(start_date = Policy_Start + dt.timedelta(days=30), end_date ="+60y");
        Time_On_Policy = round((Date_of_loss - Policy_Start).days/30)+1
        Monthly_Cost = round(float(np.random.normal(1083,300,1))/12,2)
        Total_Policy_Revenue = round(Time_On_Policy*Monthly_Cost,2)
        Sum_Insured = Total_Policy_Revenue*random.uniform(1,1.3)
        Company = fake.company2()
        Company_ID = fake.CompanyID(Company)
        if random.random() > 0.99:
            Other_Party_Name = fake.first_name()
            Other_Party_Last_Name = fake.last_name()
            Kind_Of_Loss = 'Malicious Damage'
        else:
            Other_Party_Name = None
            Other_Party_Last_Name = None
            Kind_Of_Loss = fake.loss()

        if Kind_Of_Loss != 'Theft':
            Item = 'House'
            Amount_Paid = round(random.uniform(60000,200000),2)
        else:
            Item = fake.Item()
            if Item in ['Electronics','Jewllery','More than 5 Items','Antiques']:
                Amount_Paid = round(random.uniform(50,800),2)
            else:
                Amount_Paid = round(random.uniform(30,200),2)


        Street_Address = fake.street_address()
        State = fake.state()
        City = fake.city()
        Postal_Code = fake.postalcode()
        Area = fake.Area()

        if random.random() > 0.2:
            Loss_Street_Address = Street_Address
            Loss_State = State
            Loss_City = City
            Loss_Postal_Code = Postal_Code
            Loss_Area = Area
        else:
            Loss_Street_Address = fake.street_address()
            Loss_State = fake.state()
            Loss_City = fake.city()
            Loss_Postal_Code = fake.postalcode()
            Loss_Area = fake.Area()


        info = {
        'Insured_First_Name' : fake.first_name_female(),
        'Insured_Last_Name' : fake.last_name_female(),
        'Client_ID' : ClientID,
        'Gender' : 'F',
        'Date_Of_Birth' : DOB,
        'Marital_Status' : fake.marital(),
        'Policy_Holder_Street' : Street_Address,
        'Policy_Holder_State' : State,
        'Policy_Holder_City' : City,
        'Policy_Holder_Area' : Area,
        'Policy_Holder_Postal_Code' : Postal_Code ,
        'Loss_Street' : Loss_Street_Address,
        'Loss_State' : Loss_State,
        'Loss_City' : Loss_City,
        'Loss_Area' : Loss_Area,
        'Loss_Postal_Code' : Loss_Postal_Code ,
        'Loss_Item' : Item,
        'Sum_Insured' : Sum_Insured,
        'Total_Policies_Revenue' : Total_Policy_Revenue,
        'Kind_Of_Loss' : Kind_Of_Loss,
        'Amount_Paid' : Amount_Paid,
        'Policy_Start_Date' : Policy_Start,
        'Policy_End_Date' : Policy_End,
        'Other_Party_Name' : Other_Party_Name,
        'Other_Party_Last_Name' : Other_Party_Last_Name,
        'Claim_Service_Provider': Company,
        'Broker_ID' : Company_ID,
        'Date_Of_Loss' : Date_of_loss ,
        'Fraudulent_Claim_Indicator' : 1,
        'Fraudulent_Claim_Reason' : 'Claiming shortly after opening policy'
        }
        content.append(info)
    return(content)
    
def GenerateFakeMale1(Percent):
    content = []
    for i in range(0,round(500 * Percent)):
        ClientID = int(''.join(random.sample('123456789',6)))
        DOB = fake.date_between(start_date="-90y", end_date="-20y");
        Policy_Start = fake.date_between(start_date = DOB + dt.timedelta(days=365*18), end_date = "-1d");
        Date_of_loss = fake.date_between(start_date = Policy_Start + dt.timedelta(days=1), end_date=Policy_Start + dt.timedelta(days=45));
        Policy_End = fake.date_between(start_date = Policy_Start + dt.timedelta(days=30), end_date ="+60y");
        Time_On_Policy = round((Date_of_loss - Policy_Start).days/30)+1
        Monthly_Cost = round(float(np.random.normal(1083,300,1))/12,2)
        Total_Policy_Revenue = round(Time_On_Policy*Monthly_Cost,2)
        Sum_Insured = Total_Policy_Revenue*random.uniform(1,1.3)
        Company = fake.company2()
        Company_ID = fake.CompanyID(Company)
        if random.random() > 0.99:
            Other_Party_Name = fake.first_name()
            Other_Party_Last_Name = fake.last_name()
            Kind_Of_Loss = 'Malicious Damage'
        else:
            Other_Party_Name = None
            Other_Party_Last_Name = None
            Kind_Of_Loss = fake.loss()

        if Kind_Of_Loss != 'Theft':
            Item = 'House'
            Amount_Paid = round(random.uniform(60000,200000),2)
        else:
            Item = fake.Item()
            if Item in ['Electronics','Jewllery','More than 5 Items','Antiques']:
                Amount_Paid = round(random.uniform(50,800),2)
            else:
                Amount_Paid = round(random.uniform(30,200),2)


        Street_Address = fake.street_address()
        State = fake.state()
        City = fake.city()
        Postal_Code = fake.postalcode()
        Area = fake.Area()

        if random.random() > 0.2:
            Loss_Street_Address = Street_Address
            Loss_State = State
            Loss_City = City
            Loss_Postal_Code = Postal_Code
            Loss_Area = Area
        else:
            Loss_Street_Address = fake.street_address()
            Loss_State = fake.state()
            Loss_City = fake.city()
            Loss_Postal_Code = fake.postalcode()
            Loss_Area = fake.Area()


        info = {
        'Insured_First_Name' : fake.first_name_male(),
        'Insured_Last_Name' : fake.last_name_male(),
        'Client_ID' : ClientID,
        'Gender' : 'M',
        'Date_Of_Birth' : DOB,
        'Marital_Status' : fake.marital(),
        'Policy_Holder_Street' : Street_Address,
        'Policy_Holder_State' : State,
        'Policy_Holder_City' : City,
        'Policy_Holder_Area' : Area,
        'Policy_Holder_Postal_Code' : Postal_Code ,
        'Loss_Street' : Loss_Street_Address,
        'Loss_State' : Loss_State,
        'Loss_City' : Loss_City,
        'Loss_Area' : Loss_Area,
        'Loss_Postal_Code' : Loss_Postal_Code ,
        'Loss_Item' : Item,
        'Sum_Insured' : Sum_Insured,
        'Total_Policies_Revenue' : Total_Policy_Revenue,
        'Kind_Of_Loss' : Kind_Of_Loss,
        'Amount_Paid' : Amount_Paid,
        'Policy_Start_Date' : Policy_Start,
        'Policy_End_Date' : Policy_End,
        'Other_Party_Name' : Other_Party_Name,
        'Other_Party_Last_Name' : Other_Party_Last_Name,
        'Claim_Service_Provider': Company,
        'Broker_ID' : Company_ID,
        'Date_Of_Loss' : Date_of_loss ,
        'Fraudulent_Claim_Indicator' : 1,
        'Fraudulent_Claim_Reason' : 'Claiming shortly after opening policy'
        }
        content.append(info)
    return(content)
###############################################################################
# Large claims before policy end
def GenerateFakeMale2(Percent):
    content = []
    for i in range(0,round(500 * Percent)):
        ClientID = int(''.join(random.sample('123456789',6)))
        DOB = fake.date_between(start_date="-90y", end_date="-20y"); 
        Policy_Start = fake.date_between(start_date = DOB + dt.timedelta(days=365*17), end_date = DOB + dt.timedelta(days=365*60));
        Policy_End = fake.date_between(start_date = Policy_Start + dt.timedelta(days=30), end_date ="+60y");
        Date_of_loss = fake.date_between(start_date = Policy_End + dt.timedelta(days=-45), end_date=Policy_End + dt.timedelta(days=-1));
        
        Time_On_Policy = round((Date_of_loss - Policy_Start).days/30)+1
        Monthly_Cost = round(float(np.random.normal(1083,300,1))/12,2)
        Total_Policy_Revenue = round(Time_On_Policy*Monthly_Cost,2)
        Sum_Insured = Total_Policy_Revenue*random.uniform(1,1.3)
        Company = fake.company2()
        Company_ID = fake.CompanyID(Company)
        if random.random() > 0.99:
            Other_Party_Name = fake.first_name()
            Other_Party_Last_Name = fake.last_name()
            Kind_Of_Loss = 'Malicious Damage'
        else:
            Other_Party_Name = None
            Other_Party_Last_Name = None
            Kind_Of_Loss = fake.loss()

        if Kind_Of_Loss != 'Theft':
            Item = 'House'
            Amount_Paid = round(random.uniform(Total_Policy_Revenue,Sum_Insured*1.5),2)
        else:
            Item = fake.Item()
            if Item in ['Electronics','Jewllery','More than 5 Items','Antiques']:
                Amount_Paid = round(random.uniform(1000,20000),2)
            else:
                Amount_Paid = round(random.uniform(300,2000),2)


        Street_Address = fake.street_address()
        State = fake.state()
        City = fake.city()
        Postal_Code = fake.postalcode()
        Area = fake.Area()

        if random.random() > 0.2:
            Loss_Street_Address = Street_Address
            Loss_State = State
            Loss_City = City
            Loss_Postal_Code = Postal_Code
            Loss_Area = Area
        else:
            Loss_Street_Address = fake.street_address()
            Loss_State = fake.state()
            Loss_City = fake.city()
            Loss_Postal_Code = fake.postalcode()
            Loss_Area = fake.Area()


        info = {
        'Insured_First_Name' : fake.first_name_male(),
        'Insured_Last_Name' : fake.last_name_male(),
        'Client_ID' : ClientID,
        'Gender' : 'M',
        'Date_Of_Birth' : DOB,
        'Marital_Status' : fake.marital(),
        'Policy_Holder_Street' : Street_Address,
        'Policy_Holder_State' : State,
        'Policy_Holder_City' : City,
        'Policy_Holder_Area' : Area,
        'Policy_Holder_Postal_Code' : Postal_Code ,
        'Loss_Street' : Loss_Street_Address,
        'Loss_State' : Loss_State,
        'Loss_City' : Loss_City,
        'Loss_Area' : Loss_Area,
        'Loss_Postal_Code' : Loss_Postal_Code ,
        'Loss_Item' : Item,
        'Sum_Insured' : Sum_Insured,
        'Total_Policies_Revenue' : Total_Policy_Revenue,
        'Kind_Of_Loss' : Kind_Of_Loss,
        'Amount_Paid' : Amount_Paid,
        'Policy_Start_Date' : Policy_Start,
        'Policy_End_Date' : Policy_End,
        'Other_Party_Name' : Other_Party_Name,
        'Other_Party_Last_Name' : Other_Party_Last_Name,
        'Claim_Service_Provider': Company,
        'Broker_ID' : Company_ID,
        'Date_Of_Loss' : Date_of_loss ,
        'Fraudulent_Claim_Indicator' : 1,
        'Fraudulent_Claim_Reason' : 'Large claim before policy end'
        }
        content.append(info)
    return(content)

def GenerateFakeFemale2(Percent):
    content = []
    for i in range(0,round(500 * Percent)):
        ClientID = int(''.join(random.sample('123456789',6)))
        DOB = fake.date_between(start_date="-90y", end_date="-20y"); 
        Policy_Start = fake.date_between(start_date = DOB + dt.timedelta(days=365*17), end_date = DOB + dt.timedelta(days=365*60));
        Policy_End = fake.date_between(start_date = Policy_Start + dt.timedelta(days=30), end_date ="+60y");
        Date_of_loss = fake.date_between(start_date = Policy_End + dt.timedelta(days=-45), end_date=Policy_End + dt.timedelta(days=-1));
        
        Time_On_Policy = round((Date_of_loss - Policy_Start).days/30)+1
        Monthly_Cost = round(float(np.random.normal(1083,300,1))/12,2)
        Total_Policy_Revenue = round(Time_On_Policy*Monthly_Cost,2)
        Sum_Insured = Total_Policy_Revenue*random.uniform(1,1.3)
        Company = fake.company2()
        Company_ID = fake.CompanyID(Company)
        if random.random() > 0.99:
            Other_Party_Name = fake.first_name()
            Other_Party_Last_Name = fake.last_name()
            Kind_Of_Loss = 'Malicious Damage'
        else:
            Other_Party_Name = None
            Other_Party_Last_Name = None
            Kind_Of_Loss = fake.loss()

        if Kind_Of_Loss != 'Theft':
            Item = 'House'
            Amount_Paid = round(random.uniform(Total_Policy_Revenue,Sum_Insured*1.5),2)
        else:
            Item = fake.Item()
            if Item in ['Electronics','Jewllery','More than 5 Items','Antiques']:
                Amount_Paid = round(random.uniform(1000,20000),2)
            else:
                Amount_Paid = round(random.uniform(300,2000),2)


        Street_Address = fake.street_address()
        State = fake.state()
        City = fake.city()
        Postal_Code = fake.postalcode()
        Area = fake.Area()

        if random.random() > 0.2:
            Loss_Street_Address = Street_Address
            Loss_State = State
            Loss_City = City
            Loss_Postal_Code = Postal_Code
            Loss_Area = Area
        else:
            Loss_Street_Address = fake.street_address()
            Loss_State = fake.state()
            Loss_City = fake.city()
            Loss_Postal_Code = fake.postalcode()
            Loss_Area = fake.Area()


        info = {
        'Insured_First_Name' : fake.first_name_female(),
        'Insured_Last_Name' : fake.last_name_female(),
        'Client_ID' : ClientID,
        'Gender' : 'F',
        'Date_Of_Birth' : DOB,
        'Marital_Status' : fake.marital(),
        'Policy_Holder_Street' : Street_Address,
        'Policy_Holder_State' : State,
        'Policy_Holder_City' : City,
        'Policy_Holder_Area' : Area,
        'Policy_Holder_Postal_Code' : Postal_Code ,
        'Loss_Street' : Loss_Street_Address,
        'Loss_State' : Loss_State,
        'Loss_City' : Loss_City,
        'Loss_Area' : Loss_Area,
        'Loss_Postal_Code' : Loss_Postal_Code ,
        'Loss_Item' : Item,
        'Sum_Insured' : Sum_Insured,
        'Total_Policies_Revenue' : Total_Policy_Revenue,
        'Kind_Of_Loss' : Kind_Of_Loss,
        'Amount_Paid' : Amount_Paid,
        'Policy_Start_Date' : Policy_Start,
        'Policy_End_Date' : Policy_End,
        'Other_Party_Name' : Other_Party_Name,
        'Other_Party_Last_Name' : Other_Party_Last_Name,
        'Claim_Service_Provider': Company,
        'Broker_ID' : Company_ID,
        'Date_Of_Loss' : Date_of_loss ,
        'Fraudulent_Claim_Indicator' : 1,
        'Fraudulent_Claim_Reason' : 'Large claim before policy end'
        }
        content.append(info)
    return(content)
###############################################################################   
# Many Small Claims
def GenerateFakeMale3(Percent):
    content = []
    for i in range(0,round(500 * Percent)):
        ClientID = int(''.join(random.sample('123456789',6)))
        FirstName = fake.first_name_male()
        Surname = fake.last_name_male()
        DOB = fake.date_between(start_date="-90y", end_date="-20y");
        Date_of_loss = fake.date_between(start_date = DOB + dt.timedelta(days=365*18), end_date="-1d");
        Policy_Start = fake.date_between(start_date = DOB + dt.timedelta(days=365*17), end_date = Date_of_loss);
        Policy_End = fake.date_between(start_date = Policy_Start + dt.timedelta(days=30), end_date ="+60y");
        Time_On_Policy = round((Date_of_loss - Policy_Start).days/30)+1
        Monthly_Cost = round(float(np.random.normal(1083,300,1))/12,2)
        Total_Policy_Revenue = round(Time_On_Policy*Monthly_Cost,2)
        Sum_Insured = Total_Policy_Revenue*random.uniform(1,1.3)
        Street_Address = fake.street_address()
        State = fake.state()
        City = fake.city()
        Postal_Code = fake.postalcode()
        Area = fake.Area()
        Company = fake.company2()
        Company_ID = fake.CompanyID(Company)
        for i in range(0,fake.FakeNoOfClaims()):
            
    
            if random.random() > 0.99:
                Other_Party_Name = fake.first_name()
                Other_Party_Last_Name = fake.last_name()
                Kind_Of_Loss = 'Malicious Damage'
            else:
                Other_Party_Name = None
                Other_Party_Last_Name = None
                Kind_Of_Loss = 'Theft'
    
            if Kind_Of_Loss != 'Theft':
                Item = 'House'
                Amount_Paid = round(random.uniform(60000,200000),2)
            else:
                Item = fake.Item()
                if Item in ['Electronics','Jewllery','More than 5 Items','Antiques']:
                    Amount_Paid = round(random.uniform(50,800),2)
                else:
                    Amount_Paid = round(random.uniform(30,200),2)
    
    
    
    
            if random.random() > 0.2:
                Loss_Street_Address = Street_Address
                Loss_State = State
                Loss_City = City
                Loss_Postal_Code = Postal_Code
                Loss_Area = Area
            else:
                Loss_Street_Address = fake.street_address()
                Loss_State = fake.state()
                Loss_City = fake.city()
                Loss_Postal_Code = fake.postalcode()
                Loss_Area = fake.Area()
    
    
            info = {
            'Insured_First_Name' : FirstName,
            'Insured_Last_Name' : Surname,
            'Client_ID' : ClientID,
            'Gender' : 'M',
            'Date_Of_Birth' : DOB,
            'Marital_Status' : fake.marital(),
            'Policy_Holder_Street' : Street_Address,
            'Policy_Holder_State' : State,
            'Policy_Holder_City' : City,
            'Policy_Holder_Area' : Area,
            'Policy_Holder_Postal_Code' : Postal_Code ,
            'Loss_Street' : Loss_Street_Address,
            'Loss_State' : Loss_State,
            'Loss_City' : Loss_City,
            'Loss_Area' : Loss_Area,
            'Loss_Postal_Code' : Loss_Postal_Code ,
            'Loss_Item' : Item,
            'Sum_Insured' : Sum_Insured,
            'Total_Policies_Revenue' : Total_Policy_Revenue,
            'Kind_Of_Loss' : Kind_Of_Loss,
            'Amount_Paid' : Amount_Paid,
            'Policy_Start_Date' : Policy_Start,
            'Policy_End_Date' : Policy_End,
            'Other_Party_Name' : Other_Party_Name,
            'Other_Party_Last_Name' : Other_Party_Last_Name,
            'Claim_Service_Provider': Company,
            'Broker_ID' : Company_ID,
            'Date_Of_Loss' : Date_of_loss ,
            'Fraudulent_Claim_Indicator' : 1,
            'Fraudulent_Claim_Reason' : 'Many small claims'
            }
            content.append(info)
    return(content)

def GenerateFakeFemale3(Percent):
    content = []
    for i in range(0,round(500 * Percent)):
        FirstName = fake.first_name_female()
        Surname = fake.last_name_female()
        ClientID = int(''.join(random.sample('123456789',6)))
        DOB = fake.date_between(start_date="-90y", end_date="-20y");
        Date_of_loss = fake.date_between(start_date = DOB + dt.timedelta(days=365*18), end_date="-1d");
        Policy_Start = fake.date_between(start_date = DOB + dt.timedelta(days=365*17), end_date = Date_of_loss);
        Policy_End = fake.date_between(start_date = Policy_Start + dt.timedelta(days=30), end_date ="+60y");
        Time_On_Policy = round((Date_of_loss - Policy_Start).days/30)+1
        Monthly_Cost = round(float(np.random.normal(1083,300,1))/12,2)
        Total_Policy_Revenue = round(Time_On_Policy*Monthly_Cost,2)
        Sum_Insured = Total_Policy_Revenue*random.uniform(1,1.3)
        Street_Address = fake.street_address()
        State = fake.state()
        City = fake.city()
        Postal_Code = fake.postalcode()
        Area = fake.Area()
        Company = fake.company2()
        Company_ID = fake.CompanyID(Company)
        for i in range(0,fake.FakeNoOfClaims()):
            
    
            if random.random() > 0.99:
                Other_Party_Name = fake.first_name()
                Other_Party_Last_Name = fake.last_name()
                Kind_Of_Loss = 'Malicious Damage'
            else:
                Other_Party_Name = None
                Other_Party_Last_Name = None
                Kind_Of_Loss = 'Theft'
    
            if Kind_Of_Loss != 'Theft':
                Item = 'House'
                Amount_Paid = round(random.uniform(60000,200000),2)
            else:
                Item = fake.Item()
                if Item in ['Electronics','Jewllery','More than 5 Items','Antiques']:
                    Amount_Paid = round(random.uniform(50,800),2)
                else:
                    Amount_Paid = round(random.uniform(30,200),2)
    
    
    
    
            if random.random() > 0.2:
                Loss_Street_Address = Street_Address
                Loss_State = State
                Loss_City = City
                Loss_Postal_Code = Postal_Code
                Loss_Area = Area
            else:
                Loss_Street_Address = fake.street_address()
                Loss_State = fake.state()
                Loss_City = fake.city()
                Loss_Postal_Code = fake.postalcode()
                Loss_Area = fake.Area()
    
    
            info = {
            'Insured_First_Name' : FirstName,
            'Insured_Last_Name' : Surname,
            'Client_ID' : ClientID,
            'Gender' : 'F',
            'Date_Of_Birth' : DOB,
            'Marital_Status' : fake.marital(),
            'Policy_Holder_Street' : Street_Address,
            'Policy_Holder_State' : State,
            'Policy_Holder_City' : City,
            'Policy_Holder_Area' : Area,
            'Policy_Holder_Postal_Code' : Postal_Code ,
            'Loss_Street' : Loss_Street_Address,
            'Loss_State' : Loss_State,
            'Loss_City' : Loss_City,
            'Loss_Area' : Loss_Area,
            'Loss_Postal_Code' : Loss_Postal_Code ,
            'Loss_Item' : Item,
            'Sum_Insured' : Sum_Insured,
            'Total_Policies_Revenue' : Total_Policy_Revenue,
            'Kind_Of_Loss' : Kind_Of_Loss,
            'Amount_Paid' : Amount_Paid,
            'Policy_Start_Date' : Policy_Start,
            'Policy_End_Date' : Policy_End,
            'Other_Party_Name' : Other_Party_Name,
            'Other_Party_Last_Name' : Other_Party_Last_Name,
            'Claim_Service_Provider': Company,
            'Broker_ID' : Company_ID,
            'Date_Of_Loss' : Date_of_loss ,
            'Fraudulent_Claim_Indicator' : 1,
            'Fraudulent_Claim_Reason' : 'Many small claims'
            }
            content.append(info)
    return(content)

###############################################################################
# Multiple claims for the same item with different brokers
def GenerateFakeMale4(Percent):
    content = []
    for i in range(0,round(500 * Percent)):
        DOB = fake.date_between(start_date="-90y", end_date="-20y");
        Date_of_loss = fake.date_between(start_date = DOB + dt.timedelta(days=365*18), end_date="-1d");
        Street_Address = fake.street_address()
        State = fake.state()
        City = fake.city()
        Postal_Code = fake.postalcode()
        Area = fake.Area()
      
        if random.random() > 0.99:
                Other_Party_Name = fake.first_name()
                Other_Party_Last_Name = fake.last_name()
                Kind_Of_Loss = 'Malicious Damage'
        else:
            Other_Party_Name = None
            Other_Party_Last_Name = None
            Kind_Of_Loss = fake.loss()

        if Kind_Of_Loss != 'Theft':
            Item = 'House'
            Amount_Paid = round(random.uniform(60000,200000),2)
        else:
            Item = fake.Item()
            if Item in ['Electronics','Jewllery','More than 5 Items','Antiques']:
                Amount_Paid = round(random.uniform(50,800),2)
            else:
                Amount_Paid = round(random.uniform(30,200),2)


        if random.random() > 0.2:
            Loss_Street_Address = Street_Address
            Loss_State = State
            Loss_City = City
            Loss_Postal_Code = Postal_Code
            Loss_Area = Area
        else:
            Loss_Street_Address = fake.street_address()
            Loss_State = fake.state()
            Loss_City = fake.city()
            Loss_Postal_Code = fake.postalcode()
            Loss_Area = fake.Area()
        PreviousCompany = []
        for i in range(0,random.randint(2,5)):
            Company = fake.company2()
            Company_ID = fake.CompanyID(Company)
            FirstName = fake.first_name_male()
            Surname = fake.last_name_male()
            ClientID = int(''.join(random.sample('123456789',6)))
            Policy_Start = fake.date_between(start_date = DOB + dt.timedelta(days=365*17), end_date = Date_of_loss);
            Policy_End = fake.date_between(start_date = Policy_Start + dt.timedelta(days=30), end_date ="+60y");
            Time_On_Policy = round((Date_of_loss - Policy_Start).days/30)+1
            Monthly_Cost = round(float(np.random.normal(1083,300,1))/12,2)
            Total_Policy_Revenue = round(Time_On_Policy*Monthly_Cost,2)
            Sum_Insured = Total_Policy_Revenue*random.uniform(1,1.3)
        
            if Company_ID not in PreviousCompany:
                PreviousCompany.append(Company_ID)
                info = {
                'Insured_First_Name' : FirstName,
                'Insured_Last_Name' : Surname,
                'Client_ID' : ClientID,
                'Gender' : 'M',
                'Date_Of_Birth' : DOB,
                'Marital_Status' : fake.marital(),
                'Policy_Holder_Street' : Street_Address,
                'Policy_Holder_State' : State,
                'Policy_Holder_City' : City,
                'Policy_Holder_Area' : Area,
                'Policy_Holder_Postal_Code' : Postal_Code ,
                'Loss_Street' : Loss_Street_Address,
                'Loss_State' : Loss_State,
                'Loss_City' : Loss_City,
                'Loss_Area' : Loss_Area,
                'Loss_Postal_Code' : Loss_Postal_Code ,
                'Loss_Item' : Item,
                'Sum_Insured' : Sum_Insured,
                'Total_Policies_Revenue' : Total_Policy_Revenue,
                'Kind_Of_Loss' : Kind_Of_Loss,
                'Amount_Paid' : Amount_Paid,
                'Policy_Start_Date' : Policy_Start,
                'Policy_End_Date' : Policy_End,
                'Other_Party_Name' : Other_Party_Name,
                'Other_Party_Last_Name' : Other_Party_Last_Name,
                'Claim_Service_Provider': Company,
                'Broker_ID' : Company_ID,
                'Date_Of_Loss' : Date_of_loss ,
                'Fraudulent_Claim_Indicator' : 1,
                'Fraudulent_Claim_Reason' : 'Multiple Claims at different agents'
                }
                content.append(info)
    return(content)
# Female
def GenerateFakeFemale4(Percent):
    content = []
    for i in range(0,round(500 * Percent)):
        DOB = fake.date_between(start_date="-90y", end_date="-20y");
        Date_of_loss = fake.date_between(start_date = DOB + dt.timedelta(days=365*18), end_date="-1d");
        Street_Address = fake.street_address()
        State = fake.state()
        City = fake.city()
        Postal_Code = fake.postalcode()
        Area = fake.Area()
      
        if random.random() > 0.99:
                Other_Party_Name = fake.first_name()
                Other_Party_Last_Name = fake.last_name()
                Kind_Of_Loss = 'Malicious Damage'
        else:
            Other_Party_Name = None
            Other_Party_Last_Name = None
            Kind_Of_Loss = fake.loss()

        if Kind_Of_Loss != 'Theft':
            Item = 'House'
            Amount_Paid = round(random.uniform(60000,200000),2)
        else:
            Item = fake.Item()
            if Item in ['Electronics','Jewllery','More than 5 Items','Antiques']:
                Amount_Paid = round(random.uniform(50,800),2)
            else:
                Amount_Paid = round(random.uniform(30,200),2)




        if random.random() > 0.2:
            Loss_Street_Address = Street_Address
            Loss_State = State
            Loss_City = City
            Loss_Postal_Code = Postal_Code
            Loss_Area = Area
        else:
            Loss_Street_Address = fake.street_address()
            Loss_State = fake.state()
            Loss_City = fake.city()
            Loss_Postal_Code = fake.postalcode()
            Loss_Area = fake.Area()
        PreviousCompany = []
        for i in range(0,random.randint(2,5)):
            Company = fake.company2()
            Company_ID = fake.CompanyID(Company)
            FirstName = fake.first_name_female()
            Surname = fake.last_name_female()
            ClientID = int(''.join(random.sample('123456789',6)))
            Policy_Start = fake.date_between(start_date = DOB + dt.timedelta(days=365*17), end_date = Date_of_loss);
            Policy_End = fake.date_between(start_date = Policy_Start + dt.timedelta(days=30), end_date ="+60y");
            Time_On_Policy = round((Date_of_loss - Policy_Start).days/30)+1
            Monthly_Cost = round(float(np.random.normal(1083,300,1))/12,2)
            Total_Policy_Revenue = round(Time_On_Policy*Monthly_Cost,2)
            Sum_Insured = Total_Policy_Revenue*random.uniform(1,1.3)
        
            if Company_ID not in PreviousCompany:
                PreviousCompany.append(Company_ID)
                info = {
                'Insured_First_Name' : FirstName,
                'Insured_Last_Name' : Surname,
                'Client_ID' : ClientID,
                'Gender' : 'F',
                'Date_Of_Birth' : DOB,
                'Marital_Status' : fake.marital(),
                'Policy_Holder_Street' : Street_Address,
                'Policy_Holder_State' : State,
                'Policy_Holder_City' : City,
                'Policy_Holder_Area' : Area,
                'Policy_Holder_Postal_Code' : Postal_Code ,
                'Loss_Street' : Loss_Street_Address,
                'Loss_State' : Loss_State,
                'Loss_City' : Loss_City,
                'Loss_Area' : Loss_Area,
                'Loss_Postal_Code' : Loss_Postal_Code ,
                'Loss_Item' : Item,
                'Sum_Insured' : Sum_Insured,
                'Total_Policies_Revenue' : Total_Policy_Revenue,
                'Kind_Of_Loss' : Kind_Of_Loss,
                'Amount_Paid' : Amount_Paid,
                'Policy_Start_Date' : Policy_Start,
                'Policy_End_Date' : Policy_End,
                'Other_Party_Name' : Other_Party_Name,
                'Other_Party_Last_Name' : Other_Party_Last_Name,
                'Claim_Service_Provider': Company,
                'Broker_ID' : Company_ID,
                'Date_Of_Loss' : Date_of_loss ,
                'Fraudulent_Claim_Indicator' : 1,
                'Fraudulent_Claim_Reason' : 'Multiple Claims at different agents'
                }
                content.append(info)
    return(content)
# Claiming for much larger amount than insured for
def GenerateFakeMale5(Percent):
    content = []
    for i in range(0,round(500 * Percent)):
        FirstName = fake.first_name_male()
        Surname = fake.last_name_male()
        ClientID = int(''.join(random.sample('123456789',6)))
        DOB = fake.date_between(start_date="-90y", end_date="-20y");
        Date_of_loss = fake.date_between(start_date = DOB + dt.timedelta(days=365*18), end_date="-1d");
        Policy_Start = fake.date_between(start_date = DOB + dt.timedelta(days=365*17), end_date = Date_of_loss);
        Policy_End = fake.date_between(start_date = Policy_Start + dt.timedelta(days=30), end_date ="+60y");
        Time_On_Policy = round((Date_of_loss - Policy_Start).days/30)+1
        Monthly_Cost = round(float(np.random.normal(1083,300,1))/12,2)
        Total_Policy_Revenue = round(Time_On_Policy*Monthly_Cost,2)
        Sum_Insured = Total_Policy_Revenue*random.uniform(1,1.3)
        Street_Address = fake.street_address()
        State = fake.state()
        City = fake.city()
        Postal_Code = fake.postalcode()
        Area = fake.Area()
        Company = fake.company2()
        Company_ID = fake.CompanyID(Company)
        for i in range(0,1):
            Amount_Paid = 0
            while Amount_Paid < Sum_Insured:
                
    
                if random.random() > 0.99:
                    Other_Party_Name = fake.first_name()
                    Other_Party_Last_Name = fake.last_name()
                    Kind_Of_Loss = 'Malicious Damage'
                else:
                    Other_Party_Name = None
                    Other_Party_Last_Name = None
                    Kind_Of_Loss = fake.loss()
        
                if Kind_Of_Loss != 'Theft':
                    Item = 'House'
                    Amount_Paid = round(random.uniform(60000,200000),2)
                else:
                    Item = fake.Item()
                    if Item in ['Electronics','Jewllery','More than 5 Items','Antiques']:
                        Amount_Paid = round(random.uniform(500,10000),2)
                    else:
                        Amount_Paid = round(random.uniform(300,5000),2)
        
        
        
        
            if random.random() > 0.2:
                Loss_Street_Address = Street_Address
                Loss_State = State
                Loss_City = City
                Loss_Postal_Code = Postal_Code
                Loss_Area = Area
            else:
                Loss_Street_Address = fake.street_address()
                Loss_State = fake.state()
                Loss_City = fake.city()
                Loss_Postal_Code = fake.postalcode()
                Loss_Area = fake.Area()
    
    
            info = {
            'Insured_First_Name' : FirstName,
            'Insured_Last_Name' : Surname,
            'Client_ID' : ClientID,
            'Gender' : 'M',
            'Date_Of_Birth' : DOB,
            'Marital_Status' : fake.marital(),
            'Policy_Holder_Street' : Street_Address,
            'Policy_Holder_State' : State,
            'Policy_Holder_City' : City,
            'Policy_Holder_Area' : Area,
            'Policy_Holder_Postal_Code' : Postal_Code ,
            'Loss_Street' : Loss_Street_Address,
            'Loss_State' : Loss_State,
            'Loss_City' : Loss_City,
            'Loss_Area' : Loss_Area,
            'Loss_Postal_Code' : Loss_Postal_Code ,
            'Loss_Item' : Item,
            'Sum_Insured' : Sum_Insured,
            'Total_Policies_Revenue' : Total_Policy_Revenue,
            'Kind_Of_Loss' : Kind_Of_Loss,
            'Amount_Paid' : Amount_Paid,
            'Policy_Start_Date' : Policy_Start,
            'Policy_End_Date' : Policy_End,
            'Other_Party_Name' : Other_Party_Name,
            'Other_Party_Last_Name' : Other_Party_Last_Name,
            'Claim_Service_Provider': Company,
            'Broker_ID' : Company_ID,
            'Date_Of_Loss' : Date_of_loss ,
            'Fraudulent_Claim_Indicator' : 1,
            'Fraudulent_Claim_Reason' : 'Claiming much larger than insured for'
            }
            content.append(info)
    return(content)

def GenerateFakeFemale5(Percent):
    content = []
    for i in range(0,round(500 * Percent)):
        FirstName = fake.first_name_female()
        Surname = fake.last_name_female()
        ClientID = int(''.join(random.sample('123456789',6)))
        DOB = fake.date_between(start_date="-90y", end_date="-20y");
        Date_of_loss = fake.date_between(start_date = DOB + dt.timedelta(days=365*18), end_date="-1d");
        Policy_Start = fake.date_between(start_date = DOB + dt.timedelta(days=365*17), end_date = Date_of_loss);
        Policy_End = fake.date_between(start_date = Policy_Start + dt.timedelta(days=30), end_date ="+60y");
        Time_On_Policy = round((Date_of_loss - Policy_Start).days/30)+1
        Monthly_Cost = round(float(np.random.normal(1083,300,1))/12,2)
        Total_Policy_Revenue = round(Time_On_Policy*Monthly_Cost,2)
        Sum_Insured = Total_Policy_Revenue*random.uniform(1,1.3)
        Street_Address = fake.street_address()
        State = fake.state()
        City = fake.city()
        Postal_Code = fake.postalcode()
        Area = fake.Area()
        Company = fake.company2()
        Company_ID = fake.CompanyID(Company)
        for i in range(0,1):
            Amount_Paid = 0
            while Amount_Paid < Sum_Insured:
                
    
                if random.random() > 0.99:
                    Other_Party_Name = fake.first_name()
                    Other_Party_Last_Name = fake.last_name()
                    Kind_Of_Loss = 'Malicious Damage'
                else:
                    Other_Party_Name = None
                    Other_Party_Last_Name = None
                    Kind_Of_Loss = fake.loss()
        
                if Kind_Of_Loss != 'Theft':
                    Item = 'House'
                    Amount_Paid = round(random.uniform(60000,200000),2)
                else:
                    Item = fake.Item()
                    if Item in ['Electronics','Jewllery','More than 5 Items','Antiques']:
                        Amount_Paid = round(random.uniform(500,10000),2)
                    else:
                        Amount_Paid = round(random.uniform(300,5000),2)
        
        
        
        
            if random.random() > 0.2:
                Loss_Street_Address = Street_Address
                Loss_State = State
                Loss_City = City
                Loss_Postal_Code = Postal_Code
                Loss_Area = Area
            else:
                Loss_Street_Address = fake.street_address()
                Loss_State = fake.state()
                Loss_City = fake.city()
                Loss_Postal_Code = fake.postalcode()
                Loss_Area = fake.Area()
    
    
            info = {
            'Insured_First_Name' : FirstName,
            'Insured_Last_Name' : Surname,
            'Client_ID' : ClientID,
            'Gender' : 'F',
            'Date_Of_Birth' : DOB,
            'Marital_Status' : fake.marital(),
            'Policy_Holder_Street' : Street_Address,
            'Policy_Holder_State' : State,
            'Policy_Holder_City' : City,
            'Policy_Holder_Area' : Area,
            'Policy_Holder_Postal_Code' : Postal_Code ,
            'Loss_Street' : Loss_Street_Address,
            'Loss_State' : Loss_State,
            'Loss_City' : Loss_City,
            'Loss_Area' : Loss_Area,
            'Loss_Postal_Code' : Loss_Postal_Code ,
            'Loss_Item' : Item,
            'Sum_Insured' : Sum_Insured,
            'Total_Policies_Revenue' : Total_Policy_Revenue,
            'Kind_Of_Loss' : Kind_Of_Loss,
            'Amount_Paid' : Amount_Paid,
            'Policy_Start_Date' : Policy_Start,
            'Policy_End_Date' : Policy_End,
            'Other_Party_Name' : Other_Party_Name,
            'Other_Party_Last_Name' : Other_Party_Last_Name,
            'Claim_Service_Provider': Company,
            'Broker_ID' : Company_ID,
            'Date_Of_Loss' : Date_of_loss ,
            'Fraudulent_Claim_Indicator' : 1,
            'Fraudulent_Claim_Reason' : 'Claiming much larger than insured for'
            }
            content.append(info)
    return(content)



A = GenerateMale(MalePercent)
B = GenerateFemale(FemalePercent)
C = {}
C = GenerateFakeMale1(MalePercent*0.25)
C.extend(GenerateFakeFemale1(FemalePercent*0.25))
C.extend(GenerateFakeMale2(MalePercent*0.25))
C.extend(GenerateFakeFemale2(FemalePercent*0.25))
C.extend(GenerateFakeMale3(MalePercent*0.25))
C.extend(GenerateFakeFemale3(FemalePercent*0.25))
C.extend(GenerateFakeMale4(MalePercent*0.25))
C.extend(GenerateFakeFemale4(FemalePercent*0.25))
C.extend(GenerateFakeMale5(MalePercent*0.25))
C.extend(GenerateFakeFemale5(FemalePercent*0.25))
fakedf = pd.DataFrame(C)
A.extend(B)
df = pd.DataFrame(A)

df.to_csv("LegitData2.csv")
fakedf.to_csv("FraudData2.csv")





