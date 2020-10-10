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
from sklearn import metrics

 
df=pd.read_csv('Marketing Campaign data3.csv')
df.drop(['CUST_ID'],axis=1,inplace=True)

# The function is grupping the categories of the variable Occupation
# Instead of 14 we will have 6 categories.
def OCCUPATION():
    
        df.OCCUPATION.replace(['House-s' , 'Other'],["Other","Other"],inplace=True)
        
        df.OCCUPATION.replace(['Farming', 'Transp.' ,'Handler'],["Prod_Trans_Work","Prod_Trans_Work","Prod_Trans_Work"],inplace=True)
        
        df.OCCUPATION.replace(['Crafts','Machine'],["Manual_Work","Manual_Work"],inplace=True)
        
        df.OCCUPATION.replace(['Sales','TechSup'],["Cust_Rel_Work","Cust_Rel_Work"],inplace=True)
        
        df.OCCUPATION.replace(['Protec.', 'Armed-F'],['Safty_Work','Safty_Work'],inplace=True)
        
        df.OCCUPATION.replace(['Prof.' ,'Cleric.','Exec.'],["Office_Work","Office_Work","Office_Work"],inplace=True)
             
        

OCCUPATION()

# Gropping the variable categories in 3 main categories.

def CUST_MARITAL_STATUS():
        df.CUST_MARITAL_STATUS.replace([1],["H_BeenMaried"],inplace=True)
        
        df.CUST_MARITAL_STATUS.replace([3],['NeverM'],inplace=True)
        
        df.CUST_MARITAL_STATUS.replace([2],["Married"],inplace=True)
        
CUST_MARITAL_STATUS()   

# Gropping the variable categories in 2 main categories.
def Country():
    df.COUNTRY_NAME.replace([1],['American'],inplace=True)
    
    df.COUNTRY_NAME.replace([4,  2,  5,  3, 12,  6,  8, 14,  7,  9, 11, 10, 17, 18, 13, 15,16],['Not American',
    'Not American','Not American','Not American','Not American','Not American','Not American','Not American',
    'Not American','Not American','Not American','Not American','Not American','Not American','Not American',
    'Not American','Not American'],inplace=True)
            
Country()         
    

# Gropping the variable categories in 3 main categories.

# Creating dummy variable for the categorical variables Occupation and Marital Status        
df=pd.get_dummies(df,drop_first=True)

# Ranging all the variables values from 0 to 1 
scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
df.iloc[:,:] = scaler.fit_transform(df.iloc[:,:] )



    
# Creating two different matrix for the target variable and the indipendent one    
y=df.iloc[:,df.columns == 'AFFINITY_CARD'].values.ravel()
X=df.iloc[:, df.columns != 'AFFINITY_CARD']


# Splitting the data in traing and test data.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Ranking the importance of the variable in the logistic regression
logreg = LogisticRegression()
rfe = RFE(logreg, 29)
rfe = rfe.fit(X, y)
print(rfe.support_)
print(rfe.ranking_)
 
# Running the logistic Regression with the summary
logit_model=sm.Logit(y_train,X_train)
result=logit_model.fit(maxiter=10000)
print(result.summary())


# Fit logistic regression to the training set
logreg = LogisticRegression(fit_intercept=True,solver='liblinear')
logreg.fit(X_train, y_train)

# Predict test set results 
y_pred = logreg.predict(X_test)
# Accuracy of model
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

# Confusion matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)

# Odds of the variable 
print( np.exp(result.params))

# Predictive probability of the test data 
print(logreg.predict_proba(X_test))

# Creating ROC curve
logit_roc_auc = roc_auc_score(y_test, logreg.predict(X_test))
fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(X_test)[:,1])
plt.figure()
plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
# Plot base line
plt.plot([0, 1], [0, 1],'r--')
# Set axis limit for x-axis and y-axis
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
# Label axis
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
# Save the ROC graph
plt.savefig('Log_ROC')
# Plot the ROC graph 
plt.show()
 




