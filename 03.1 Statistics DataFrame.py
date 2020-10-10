import csv
import pandas as pd
import numpy as np
import scipy.stats
import matplotlib
import matplotlib.pyplot as plt
from scipy.spatial import distance

df=pd.read_csv('Marketing Campaign data3.csv')
df.drop(['OCCUPATION'],axis=1,inplace=True)
      
def Stat_Variables(prompt):
    x=dict(pd.Series(df.columns))
    while True:
        try:
            y=int(input(prompt))
            if y in x:
                print("You selected the variable: "+"\n"+"\n"
                "<<<<<<"+"  " + x.get(y) +"  "+"!!!"+ ">>>>>","\n")
                print("This is a short statistics Summary","\n")
                print(df5[x[y]]) 
                return(y)
            elif y==14:
                break       
            else :
                print("Ooopss !!!! there is an ERROR !!!" +"\n \n"+ "The variable: " +"<<<< "+ str(y) + " >>>> " +" " +"\n"+ 
                       "is not in the list of the variables,please","insert a value that is in the range (0-12)") 
        except Exception : 
                 print('<<<<<'+ "Sorry !!!"+'>>>>>'+"\n" +"The variable is not a number,please "
                       "insert a value in range (0-12)")   
a=pd.Series(df.sum(axis=0)) 
b=pd.Series(df.mean(axis=0)) 
c=pd.Series(df.std(axis=0)) 
d=pd.Series(df.skew(axis=0))
e=pd.Series(df.kurt(axis=0))
stats=[a,b,c,d,e]
   
df5=pd.DataFrame(stats,index=['Sum','Mean','St','Skw','Kurt'],columns=df.columns)       
                             
Stat_Variables('0  CUST_ID'+'\n'+'1  CUST_GENDER'+'\n'+ '2  AGE'+'\n'+ '3  CUST_MARITAL_STATUS'+'\n'+ '4  COUNTRY_NAME'+'\n'+
               '5  CUST_INCOME_LEVEL'+'\n'+ '6  EDUCATION'+'\n'+ '7  HOUSEHOLD_SIZE'+'\n'+'8  YRS_RESIDENCE' +'\n'+
               '9  AFFINITY_CARDR'+'\n'+ '10  BULK_PACK_DISKETTES'+'\n'+'11  FLAT_PANEL_MONITOR'+'\n'+
               '12  HOME_THEATER_PACKAGE'+'\n'+'13  BOOKKEEPING_APPLICATION''\n'+
               "<<<<< 14  TO EXIT From the PROGRAM >>>>>" +'\n \n'+"Please enter the number of the variable from the list above,values are"+ 
                ' ' +"in range (0-14) or type 14 TO EXIT from the program:"+"\n") 
 
