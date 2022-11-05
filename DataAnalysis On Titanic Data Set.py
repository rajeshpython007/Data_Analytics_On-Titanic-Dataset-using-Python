#!/usr/bin/env python
# coding: utf-8

# # Data Analysis On Titanic Dataset

# In[13]:


import pandas as pd
import matplotlib as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


df=pd.read_csv("E:\\DATA SCIENCE\\Project\\python\\titanic.csv")


# In[66]:


df.head(50)


# In[86]:


df.columns


# # PRINTING THE COMPLETE DETAILS

# In[11]:


df.info()


# # PRINTING THE COLUMNS

# In[21]:


for col in df.columns:
    print(col)


# # PRINTING THE MODE OF AGE 

# In[26]:


df.Age.mode()


# # PRINTING THE MEAN OF AGE

# In[29]:


df.Age.mean()


# # PRINTING THE MEDIAN OF AGE

# In[30]:


df.Age.median()


# # PRINTING THE UNIQUE AGE

# In[32]:


df.Age.unique()


# # PRINTING THE COUNT OF NULL VALUES IN AGE COLUMN

# In[36]:


df.Age.isnull().count()


# # PRINTING THE COUNT OF NULL VALUES IN AGE COLUMN

# In[40]:


df.Age.count()


# # PRINTING THE MAXIMUM VALUE OF EACH COLUMN

# In[41]:


df.max()


# # PRINTING THE MINIMUM VALUE IN EACH COLUMN

# In[42]:


df.min()


# # PRINTING THE SUM OF NULL VALUES IN EACH COLUMN

# In[44]:


df.isnull().sum()


# # PRINTING THE COUNT OF NULL VALUE IN EACH COLUMN

# In[45]:


df.isnull().count()


# # PRINTING THE MAXIMUM FARE PAID BY EACH CUSTOMER

# In[58]:


df.groupby('Name').max('Fare')


# # FINDING THE UNIQUE VALUES FROM COLUMN : SEX

# In[69]:


df.Sex.unique()


# # Describe : Count | Unique | Top | Frequence  of Name & Age column 

# In[71]:


df.Name.describe()


# In[72]:


df.Age.describe()


# # Displaying and counting all the Categorical value of categorical column :  name 

# In[74]:


df.Name.unique()


# In[78]:


df.Name.nunique()


# # Mode of Categorical Values of Name Column

# In[79]:


df.Name.mode()


# # Finding the number of unique values in Fare Column 

# In[87]:


df.Fare.nunique()


# # Number Of Rows and Columns

# In[115]:


df.shape


# # Customer Paid Highest Amount of Fare

# In[130]:


fare=pd.DataFrame(df.groupby('Name').max(numeric_only=True)['Fare'])
fare.sort_values(by=['Fare'],ascending=False, inplace = True)
fare.head(1)


# # Customer Paid Lowest Amount of Fare

# In[133]:


fare=pd.DataFrame(df.groupby('Name').min(numeric_only=True)['Fare'])
fare.sort_values(by=['Fare'],ascending=False, inplace = True)
fare.tail(1)


# # Customer having highest age who Paid Lowest Amount of Fare

# In[144]:


fare=pd.DataFrame(df.groupby('Age').min(numeric_only=True)['Fare'])
fare.sort_values(by=['Fare'],ascending=False, inplace = True)
fare.tail(1)


# In[146]:


fare=pd.DataFrame(df.groupby('Age').max(numeric_only=True)['Fare'])
fare.sort_values(by=['Fare'],ascending=False, inplace = True)
fare.head(1)


# We found the passengers from same age has paid both maximum and minimum Fare. 

# # Displaying The Person and respective age who paid maximum Fare.

# In[155]:


fare=pd.DataFrame(df.groupby(['Name','Age']).max(numeric_only=True)['Fare'])
fare.sort_values(by=['Fare'],ascending=False, inplace = True)
fare.head(1)       


# # Displaying The Person and respective age who paid minimum Fare.

# In[156]:


fare=pd.DataFrame(df.groupby(['Name','Age']).min(numeric_only=True)['Fare'])
fare.sort_values(by=['Fare'],ascending=False, inplace = True)
fare.tail(1)  


# # Removing all the Null/NaN/NaT Values

# In[157]:


df.dropna()


# # Droping All Columns with Any Missing Value

# In[159]:


df.dropna(axis=1)


# # Drop Row/Column Only if All the Values are Null

# In[164]:


df1 = df.dropna(how='all', axis=1)
print(df1)


# # Deleting all duplicates & Null/NaN/NaT Values & Missing Values

# In[169]:


df.dropna().drop_duplicates(keep=False).dropna(axis=1)
#drop_duplicates(keep=False) - Drop Duplicates
#dropna(axis=1) - Drop Missing Values


# # FILLING ALL THE NAN VALUES WITH 0

# In[58]:


df.fillna(0)


# # REPLACING NULL VALUES WITH THE MODE IN CABIN COLUMN

# In[60]:


a=df.Fare.fillna(df.Fare.mode()[0],inplace=True) #inplace is to make the changes permanently
print(a)


# we are getting none coz : we dont have any null value here.

# In[51]:


df.isnull()


# # Removing the Duplicates from Name  & Age Column

# In[171]:


df.drop_duplicates(subset=['Name', 'Age'])


# In[178]:


df.groupby(['Name']).Fare.agg(['mean','count'])


# # Setting PassengerId as an Index or Row Label.

# In[184]:


df.set_index('PassengerId')


# # Reseting the assigned index earlier.

# In[43]:


df.reset_index()


# # DISPLAYING NEW INDEX 

# In[44]:


df.reset_index(drop=True)


# # Displaying Name and Fare column and number of rows as desired.

# In[20]:


df.loc[0:4,["Name","Fare"]]


# # DISPLAYING FARE PAID BY PARTICULAR CUSTOMER

# In[21]:


df.loc[3,'Fare']


# # DISPLAYING PARTICULAR COLUMN RANGE

# In[26]:


df.loc[0:4,'Name':'Fare'] #0:4=> ROW  and column name range: 1st column is name will go upto Fare column.


# In[33]:


df.iloc[0:5,3:10]


# # USING .iloc & .loc

# In[35]:


df.iloc[3,9]


# In[36]:


df.loc[3,'Fare']


# # DISPLAYING PARTICULAR COLUMN

# In[28]:


df.iloc[1:4,3:4]


# # SORTING WHOLE DATAFRAME VALUE BY FARE

# In[29]:


df.sort_values(by=['Fare'])


# # Adding 1 to everyone's Fare that they have paid.

# In[38]:


df['Fare'].apply(lambda x: x+1)


# # REPLACING THE 'MALE&FEMALE' with '1 & 0' RESPECTIVELY.
# #Map Function is used.

# In[42]:


df['Sex'].map({'male':1,'female':0})


# # ENCODING BY USING MAP FUNCTION: REPLACING FARE <=50 :0 , 50< : 1 

# In[79]:


def my_function(x): 
 if x <= 50:
     return('0')
 if x > 50:
    return ('1')
df["Fare"].map(my_function)


# # Age distribution of Titanic Passengers

# In[76]:


df.Age.hist()


# # DISPLAYING DETAILS OF THE VLUES BY APPLYING CONDITIONS

# In[90]:


df.loc[df['Fare']==30.0000]


# # Finding the DETAILS of ALL THE VALUES HAVING FARES > 260

# In[99]:


df.loc[df['Fare']>260]


# # FIND THE NAMES HAVING 'EMI' IN THEM

# In[104]:


df.loc[df['Name'].str.contains('emi')]


# # FIND THE NAMES NOT HAVING 'EMI' IN THEM

# In[106]:


df.loc[~df.Name.str.contains('emi')]


# # FIND THE NAMES STARTS WITH 'A'

# In[107]:


df.loc[df.Name.str.startswith('A')]


# # FIND THE NAMES ENDS WITH 'A'

# In[109]:


df.loc[df.Name.str.endswith('A')]


# In[120]:


df["Mine"]='None'
df

