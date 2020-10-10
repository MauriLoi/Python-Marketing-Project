import csv
import pandas as pd  
import numpy as np
import scipy.stats
import matplotlib
import matplotlib.pyplot as plt
from scipy.spatial import distance

df3=pd.read_csv('Marketing Campaign data3.csv')
df3.drop(['OCCUPATION'],axis=1,inplace=True)
variables=pd.Series(df3.columns)
dict_variables=dict(variables)
x=dict_variables
  

def Histog(prompt):
        
        variables=pd.Series(df3.columns)
        dict_variables=dict(variables)
        x=dict_variables
        
        while True :
         try: 
                y=int(input(prompt))
                
                if y in x:
                    print("You selected the variable: "+"\n"+"\n"
                    "<<<<<<"+"  " + x.get(y) +"  "+"!!!"+ ">>>>>","\n")
                    print("This is a Frequency Histogram ","\n")
                   
                    a=df3[x[y]]
                    #c=np.array(a)           
                    #plt.hist(c)
                    #print(a.value_counts().plot(kind='hist'))
                    print(a.plot(kind='hist'))
                    plt.show()
                    #print(a.value_counts().plot(kind='bar'))
                    #plt.show()
                    return(y)
                   
                          
                else :
                    print("Ooopss there is an ERROR !!!" +"\n"+"\n"+ "The variable: "+"\n" +"<<<< "+ str(y) + " >>>> " +" " +"\n"+ 
                       "is not in the list of the variables,please","insert a value that is in the range (0-12)") 
                    
         
         except Exception : 
                 print("Sorry !!!"+"\n" +"the variable is not a number,please "
                       "insert a value in range (0-13)")                   
                 
                       
Histog('0  CUST_ID'+'\n'+'1  CUST_GENDER'+'\n'+ '2  AGE'+'\n'+ '3  CUST_MARITAL_STATUS'+'\n'+'4  COUNTRY_NAME'+'\n'+ 
               '5  CUST_INCOME_LEVEL'+'\n'+'6  EDUCATION'+'\n'+ '7  HOUSEHOLD_SIZE'+'\n'+ '8  YRS_RESIDENCE'+'\n'+ 
               '9  AFFINITY_CARD'+'\n'+'10  BULK_PACK_DISKETTES' +'\n'+'11  FLAT_PANEL_MONITOR'+'\n'+ 
               '12  HOME_THEATER_PACKAGE'+'\n'+'13  BOOKKEEPING_APPLICATION' +'\n \n'+"Please insert the number of the variable:")             






