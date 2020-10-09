import csv
import pandas as pd
import numpy as np
 
 
 
df = pd.read_csv('Marketing Campaign data.csv')

print(df.head(10))                                           #Is printing the first 10 rows of the data frame
print(df.shape)                                              #Is returning the shape of the DataFrame
print(df.dtypes)                                            #Is returning the types of values for each column

print(df.info())                                             #Is returning a summary of the DataFrame
print(df.get_dtype_counts())                                 #Is returning the count of the data types for all the data frame

 
#Is returning the count list of the unique value for each variables in df.
#With a for loop for all the column returning the list and the frequency of 
#evrey single value present in that column in  descending order and the finial sum of the overall frequency of observation for each column

def unique_value_Columns():                                  
      col=list(df.columns)
      for i in col:
          a=df[i].value_counts()
          print(pd.Series(a))
          
unique_value_Columns()








         