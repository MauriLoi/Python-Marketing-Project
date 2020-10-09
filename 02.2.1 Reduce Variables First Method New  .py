import csv
import pandas as pd  
import numpy as np

 
df=pd.read_csv('Marketing Campaign data1.csv')
 
                                                                 # Using the crosstab function from pandas i have defined a new function tha will return 
                                                                 # a contingency table, a two-wayfrequency table. Each of the variable will be used as a dimension
                                                                 # and compared with the target variable AFFINITY_CARD.
                                                                 # Two-way tables can give you insight into the relationship between two variables         
                         
def crosstab():
    col_names=['CUST_GENDER','AGE','CUST_MARITAL_STATUS','COUNTRY_NAME',
    'CUST_INCOME_LEVEL','EDUCATION','OCCUPATION','HOUSEHOLD_SIZE',
    'YRS_RESIDENCE','BULK_PACK_DISKETTES','FLAT_PANEL_MONITOR',
    'HOME_THEATER_PACKAGE','BOOKKEEPING_APPLICATION','PRINTER_SUPPLIES','Y_BOX_GAMES','OS_DOC_SET_KANJI']
    
    for i in col_names:
         Frequency=pd.crosstab(index=df[i], columns=df['AFFINITY_CARD'],margins=True,normalize=True) 
         print(Frequency)
         
     
crosstab()                                                                
#First Method 
#Drop Column from data frame with drop() function 


df.drop(['PRINTER_SUPPLIES','Y_BOX_GAMES','OS_DOC_SET_KANJI','COMMENTS'],axis=1,inplace=True)

df.to_csv('Marketing Campaign data2.csv',index=False)







