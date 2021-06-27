import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
%matplotlib inline 

df = pd.read_csv("company_financials.csv")

print(df.head())

print(df.info())

correlation1 = df.corr()
print(correlation1)

sns.histplot(data=df['Price/Sales'],bins=30,kde=False)

sns.scatterplot(data=df['EBITDA'])

df = pd.get_dummies(data=df,columns=['Sector'],drop_first=True)
plt.figure(figsize=(18,16))
sns.heatmap(df.corr(),annot=True,cmap='coolwarm')

df['Price/Earnings'].mean()

df["Price/Earnings"].fillna("24.808389662027817", inplace = True)

df['Price/Earnings'].isnull().sum()

df.isnull().sum()

df['Price/Book'].isnull().sum()

df['Price/Book'].mean()

sns.scatterplot(x=df['Price/Book'],y=df['Price'])

df["Price/Book"].fillna("8", inplace = True)

print(df.isnull().sum())
