import csv
import pandas as pd  
import numpy as np
import scipy.stats
import matplotlib
import matplotlib.pyplot as plt
from scipy.spatial import distance
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler

df=pd.read_csv('Marketing Campaign data3.csv')
df.drop(['OCCUPATION'],axis=1,inplace=True)
# Standardizing the values of the data frame
cols = df.iloc[:,1:]
for i in cols:
        col_zscore = i 
        df[col_zscore] = (df[i] - df[i].mean())/df[i].std(ddof=1)
#Declering the global variables
z=list(df['CUST_ID'])
number=[]
List=[1]
max_number=1
# Adding to number[] the Id value if present in z,printing the traspose series, breaking the loop and running exceptions
def Distance1():
            while len(number)<=max_number  : 
                try:
                   global ID
                   ID=int(input("Please insert the Costumer Id in range (101501-103000) with"+
                   "a step of 1 or Insert the number 0 to close the program:"))
                   if ID in z  :   
                        ss=df[df['CUST_ID'] ==ID]            
                        ss1=np.array(ss)
                        ss2=ss.T
                        number.append(ID)
                        print("The Customer ID you selected is:"+"\n"+
                        "<<<<"+ str(ID) +">>>>"+"\n"+ 'and the value of the variabl are:',"\n")
                        print(ss2,"\n")
                   elif ID==0:
                        break
                   else: 
                      print("The Customer ID is not present in the list:")  
                except Exception:
                      print("Sorry !!!"+"\n" +"the Customer ID is not a number,please ",
                       "insert a value in range (101501-103000)") 
Distance1()
# Printing the eucledian distance 
def Distance():
 for i in List:
     if ID in z:
            print("The Eucledian Distance among the customer "+ str(number[0]) +" "+
            "and the customer"+" "+ str(number[1]) + " is:","\n")
            ss3=df[df['CUST_ID'] ==number[0]] 
            ss4=df[df['CUST_ID'] ==number[1]]
            print(distance.euclidean(ss3,ss4))
Distance()

 