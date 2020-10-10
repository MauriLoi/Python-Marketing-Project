import csv
import pandas as pd  
import numpy as np
 
df=pd.read_csv('Marketing Campaign data2.csv')######  CUST_GENDER   ##########
  
######  CUST_GENDER   ##########

# First Method Replace
print(df["CUST_GENDER"].value_counts()) 

df["CUST_GENDER"].replace(["M","F"],[1,0], inplace=True)                         # Using the replace function the value "M" and "F"
                                                                                  # are replaced with the new values 1 and 0.
                                                                                # 1 for "M" and 0 for "
print(df.groupby(df.CUST_GENDER).size())                                                                                 


######  COUNTRY_NAME   ##########
print(df["COUNTRY_NAME"].value_counts())

# First Method Replace

df["COUNTRY_NAME"].replace(['United States of America','Argentina','Italy',              # Using the replace function the list of values of the column "COUNTRY_NAME" ordered by frequncy 
'Brazil','Germany','Poland','United Kingdom','Saudi Arabia','Canada' ,                   # are replaced with the new values from 1 to 18.
'Denmark','Singapore','New Zealand','China','Japan','Turkey','Spain',                    
'South Africa','France'],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], inplace=True)  

print(df.groupby(df.COUNTRY_NAME).size())                                                                              




######  CUST_INCOME_LEVEL   ##########
print(df.groupby(df.CUST_INCOME_LEVEL).size())

#First Method Replace

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
         
        #print(df.groupby(df.CUST_INCOME_LEVEL).size())
CUST_INCOME_LEVEL()
print(df.groupby(df.CUST_INCOME_LEVEL).size())

######  EDUCATION   ##########

print(df["EDUCATION"].value_counts()) 

#First Method Replace

df["EDUCATION"].replace(['Presch.','1st-4th','5th-6th',                                 # Using the replace function the list of values of the column ""EDUCATION" ordered from 
'7th-8th','9th','10th','11th','12th','HS-grad' ,                                        # the lowest to th higher level.Are replaced with the list of number from 1 to 16.
'Assoc-A','Assoc-V','< Bach.','Bach.','Profsc','Masters','PhD'],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], inplace=True)

print(df.groupby(df.EDUCATION).size())



######  HOUSEHOLD_SIZE   ##########
a=(df["HOUSEHOLD_SIZE"].value_counts()) 
print(pd.Series((a)))
 
#First Method Replace

df["HOUSEHOLD_SIZE"].replace(['1','2','3',                        # Using the replace function the list of values present in the "HOUSEHOLD_SIZE" column 
'4-5','6-8','9+'],[1,2,3,4,5,6], inplace=True)                    # ordered by the size of the house are replaced with the list of number from 1 to 6.


print(df.groupby(df.HOUSEHOLD_SIZE).size())

######  CUST_MARITAL_STATUS   ##########

def CUST_MARITAL_STATUS():
    levels=['NeverM', 'Married', 'Divorc.', 'Mabsent', 'Separ.', 'Widowed']
    for i in levels  :
        if i == 'Divorc.'and 'Mabsent'and 'Separ.'and 'Widowed':
            df.CUST_MARITAL_STATUS.replace(['Divorc.','Mabsent','Separ.','Widowed'],[1,1,1,1],inplace=True)
        if i == 'NeverM':
            df.CUST_MARITAL_STATUS.replace(['NeverM'],[3],inplace=True)
        if i == 'Married' :
           df.CUST_MARITAL_STATUS.replace(['Married'],[2],inplace=True)
        
        
CUST_MARITAL_STATUS()  



df.to_csv('Marketing Campaign data3.csv',index=False)
                                           
                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 