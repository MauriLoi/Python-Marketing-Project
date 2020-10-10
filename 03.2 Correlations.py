import csv
import pandas as pd  
import numpy as np
import scipy.stats
import matplotlib
import matplotlib.pyplot as plt
from scipy.spatial import distance
import statsmodels.api as sm
import seaborn as sns
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.feature_selection import RFECV
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import MinMaxScaler
#from mlxtend.preprocessing import standardize
from sklearn import metrics
 

df=pd.read_csv('Marketing Campaign data3.csv')

df.drop(['OCCUPATION','CUST_ID'],axis=1,inplace=True)

cols = df[:]
for i in cols:
    col_zscore = i 
    df[col_zscore] = (df[i] - df[i].mean())/df[i].std(ddof=1)
     
 

def Correlation(Variable):
          correl=df.corr()[Variable]
          sort=correl.sort_values(ascending=True)
          print("The Correlation among the variable AFFINITY_CARD and,"+
          "all the other variables is in the table below:","\n") 
          print(sort)
          
Correlation("AFFINITY_CARD")

sns.heatmap(df.corr(),annot=True,fmt=".2f")
plt.show()




