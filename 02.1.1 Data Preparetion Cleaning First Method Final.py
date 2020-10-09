import csv
import pandas as pd  
import numpy as np


#Download the csv file from the directory
df = pd.read_csv('Marketing Campaign data.csv')
 
# Analysis and count of the rows to clean

print("The number of Nan in the Dataframe for each colum are:"+"\n")                                                                 
print(df.apply(lambda x: sum(x.isnull().values), axis = 0))               #Returning the count of missing value in each column(Variables)
print("The number of Nan in the colum COMMENTS is:"+"\n")  
print(df['COMMENTS'].isnull().sum())                                      #Returning the count of missing value in column(COMMENTS)

print("The number of ? in the colum OCCUPATION is:"+"\n")
Value_to_clean=(df['OCCUPATION'] == "?")                                  #Returning the count of the rows that contain the value "?"
print(Value_to_clean.sum()) 


print("The rows with Nan values and ? are:"+"\n")                         # Using variable attributes
print(df[df['COMMENTS'].isnull() & (df['OCCUPATION'] == "?")])            # Is a good idea to check before cleaning all the rows from the data frame with "?" string value in it 
Value_to_clean_comb=df['COMMENTS'].isnull() & (df['OCCUPATION'] == "?")   # the quantity of rows with a combined value of Nan and "?" in the data frame.
print("\n"+"The number of row with NaN and ? is :"+"\n"
+ str(Value_to_clean_comb.sum()))                                         # The quantity is 4.


#Frist method Data.Frame.dropna()
#Drop_null Function


def drop_null() :                                               #Define a function that cheks if the sum of empty value                                                            
    global df
    if df.isnull().any(axis=1).sum()>0 :                        #for all the colummns is > di 0.
           
           df=df.dropna()                                       #If isnull().sum() >0 drops(remove) all the the rows with empty
           print("The number of Nan after cleaning is:")
           print(df.isnull().any(axis=1).sum())                 #and return a new DataFrame df cleaned.
           print("The shape of the new DataFrame without Nan is :")
           print(df.shape)                                      #If isnull().sum() =0 is returning a new DataFrame df1 uqual to df(previuos DataFrame) 
    else :
           df=df
           #return(df1.isnull().any(axis=1).sum())   
           print("The number of Nan is:")
           print(df.isnull().any(axis=1).sum())
           print(df.shape) 
drop_null()

#Frist method Revoing '?' value
#Drop a row if it contains a certain value

df = df[df.OCCUPATION != '?']                                   # Starting from df the previous data frame defined as df(global data frame inside the function) minus all the rows with 
print("The shape of the new DataFrame after remuoving",         
       "Nan and ? is :")
print(df.shape)                                                 # null values we are defining the new data frame df equal to df(1427, 19) minus all the rows in the dataframe  
                                                                # where the "?" is present as a value.
                                                                # df is the new data frame of 1351( rows), 19(columns). 1500 - 73 (Nan) - 76("?"),76 and not 80 becouse 4 rows 
                                                                # with "?" have been already canceled when we have removed the Nan value.

 
Value_to_clean_comb=df['COMMENTS'].isnull() & (df['OCCUPATION'] == "?")
print("\n"+"The number of row with NaN and ? is :"+"\n"
+ str(Value_to_clean_comb.sum()))

 
df.to_csv('Marketing Campaign data1.csv',index=False) 


                                                                
