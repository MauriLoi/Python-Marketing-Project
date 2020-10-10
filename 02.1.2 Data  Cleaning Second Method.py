import csv
import pandas as pd  
import numpy as np


df=pd.read_csv('Marketing Campaign data.csv')

#First Method Fillin() and Drop()

def Fillin_and_Drop():
    
    df.fillna("NaN",inplace=True)                             # With the method fillin() all the NaN value in df["COMMENT"] 
    df.drop(df[(df.OCCUPATION=="?")].index,inplace=True)      # are replaced with the string  "NaN".
    df.drop(df[(df.COMMENTS=="NaN")].index,inplace=True)      # With the method drop() the rows with the values "?" and "NaN"
    print("The shape of the new DataFrame is :"+"\n")
    print(df.shape)                                           # are dropped. 

Fillin_and_Drop()

 

df.to_csv('Marketing Campaign data1.csv',index=False)


