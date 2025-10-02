import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("COVID.csv")
#Basic informations about dataset
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())
print(df.describe())

#Remove unnecessary columns
df = df.drop(columns=['SNo','Last Update','Province/State'])

#Remove duplicates
df = df.drop_duplicates()

#Remove negatives values and zeros
print("Negative values\n",(df[['Recovered','Deaths','Confirmed']] < 0).sum())
df = df[(df['Confirmed'] > 0) & (df['Deaths'] > 0) & (df['Recovered'] > 0)]
df = df.reset_index(drop=True)
df.to_excel("updatecovid.xlsx")
print(df)
