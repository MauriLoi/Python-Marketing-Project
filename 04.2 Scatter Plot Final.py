import csv
import pandas as pd  
import numpy as np
import scipy.stats
import matplotlib
import matplotlib.pyplot as plt
from scipy.spatial import distance

df=pd.read_csv('Marketing Campaign data3.csv')

df.drop(['OCCUPATION'],axis=1,inplace=True)

x=dict(pd.Series(df.columns))
z=list(pd.Series(df.columns))
number=[]
max_number=1
 
def Scatter(prompt):
             while len(number)<=max_number:
                try:
                   global ID
                   ID=int(input(prompt))
                   
                   if ID in x : 
                       number.append(ID)
                       print('The Customer ID you selected is:'+"\n"+"    <<<<"+ z[ID] +">>>>")
                   
                   else: 
                      print("Ooopss !!!! there is an ERROR !!!" +"\n \n"+ "The variable: " +"<<<< "+ str(ID) + " >>>> " +" " +"\n"+ 
                       "is not in the list of the variables,please","insert a value that is in the range (0-13)")
                     
                except Exception :
                     print('<<<<<'+ "Sorry !!!"+'>>>>>'+"\n" +"The variable is not a number,please "
                       "insert a value in range (0-13)") 
                     
Scatter('0  CUST_ID'+'\n'+'1  CUST_GENDER'+'\n'+ '2  AGE'+'\n'+ '3  CUST_MARITAL_STATUS'+'\n'+'4  COUNTRY_NAME'+'\n'+ 
               '5  CUST_INCOME_LEVEL'+'\n'+'6  EDUCATION'+'\n'+ '7  HOUSEHOLD_SIZE'+'\n'+ '8  YRS_RESIDENCE'+'\n'+ 
               '9  AFFINITY_CARD'+'\n'+'10  BULK_PACK_DISKETTES' +'\n'+'11  FLAT_PANEL_MONITOR'+'\n'+ 
               '12  HOME_THEATER_PACKAGE'+'\n'+'13  BOOKKEEPING_APPLICATION' +
               '\n \n'+"Please insert the number of the variable in range (0-13) :")
          
print("The Scatter plot of the variable "+ z[ID] +" "+"and the variable"+" "+ z[ID] + " is:","\n")
df.plot(kind='scatter', x=number[0], y=number[1])
plt.title(x[number[0]] +' '+'vs'+' '+ x[number[1]]+' '+'Scatter Plot',fontsize=10)
plt.xlabel(x[number[0]])
plt.ylabel(x[number[1]])
plt.show()
plt.show()

