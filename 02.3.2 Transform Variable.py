import csv
import pandas as pd  
import numpy as np

df=pd.read_csv('Marketing Campaign data1.csv')



######  CUST_GENDER   ##########

# Second Method 
df["CUST_GENDER"]= df["CUST_GENDER"].apply({"M":1, 'F':0}.get)


######  COUNTRY_NAME   ##########

def Country_Ordinal():
    Country=df["COUNTRY_NAME"].value_counts(ascending=False)
    Country_Keys=list(Country.index)
    Countr_Value=list(range(1,19))
    Country_Ord_Dic={}
    for i in range(0,18):
    
       Country_Ord_Dic[Country_Keys[i]]=Countr_Value[i]
    
    df.COUNTRY_NAME = [Country_Ord_Dic[i] for i in df.COUNTRY_NAME]       
    print(df.COUNTRY_NAME.value_counts())
Country_Ordinal()

######  CUST_INCOME_LEVEL   ##########


def CUST_INCOME_LEVEL():
    levels=['A: Below 30,000' ,'B: 30,000 - 49,999','C: 50,000 - 69,999','D: 70,000 - 89,999','E: 90,000 - 109,999',                  # Define the list of levels in the column "CUST_INCOME_LEVEL"
             'F: 110,000 - 129,999','G: 130,000 - 149,999','H: 150,000 - 169,999','I: 170,000 - 189,999','J: 190,000 - 249,999',
             'J: 190,000 - 249,999','K: 250,000 - 299,999','L: 300,000 and above']
    for i in levels  :                        
        if i == 'A: Below 30,000'or'B: 30,000 - 49,999' :                                                                             # Fro loop with if statments that replace the specific values if present in the  
           df.CUST_INCOME_LEVEL.replace(['A: Below 30,000' ,'B: 30,000 - 49,999'],[1,1],inplace=True)                                 # levels list with the number from 1 to 5.
        if i == 'C: 50,000 - 69,999'or'D: 70,000 - 89,999'or'E: 90,000 - 109,999':
            df.CUST_INCOME_LEVEL.replace(['C: 50,000 - 69,999','D: 70,000 - 89,999','E: 90,000 - 109,999'],[2,2,2],inplace=True)
        if i == 'F: 110,000 - 129,999'or'G: 130,000 - 149,999':
            df.CUST_INCOME_LEVEL.replace(['F: 110,000 - 129,999','G: 130,000 - 149,999'],[3,3],inplace=True)
        if i == 'H: 150,000 - 169,999'or'I: 170,000 - 189,999'or'J: 190,000 - 249,999'or'K: 250,000 - 299,999':
            df.CUST_INCOME_LEVEL.replace(['H: 150,000 - 169,999','I: 170,000 - 189,999','J: 190,000 - 249,999','K: 250,000 - 299,999'],[4,4,4,4],inplace=True)
        if i== 'L: 300,000 and above':
            df.CUST_INCOME_LEVEL.replace(['L: 300,000 and above'],[5],inplace=True)
         
CUST_INCOME_LEVEL()
######  EDUCATION   ##########


df["EDUCATION"]= df["EDUCATION"].apply({'Presch.':1,'1st-4th':2,'5th-6th':3,'7th-8th':4,'9th':5,'10th':6,'11th':7,'12th':8,'HS-grad':9 ,
'Assoc-A':10,'Assoc-V':11,'< Bach.':12,'Bach.':13,'Profsc':14,'Masters':15,'PhD':16}.get)


######  HOUSEHOLD_SIZE   ##########

df['HOUSEHOLD_SIZE']= df["HOUSEHOLD_SIZE"].apply({'1':1, '2':2,'3':3,'4-5':4,'6-8':5,'9+':6}.get)



