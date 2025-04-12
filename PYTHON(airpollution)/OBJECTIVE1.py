#cleaning of data
import numpy as nm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("UNCLEANED.csv")
df.head(10)
print(df.head().to_string())
print(df.describe())
print(df.shape)
#removing null values
print("Missing value in each column:\n")
print(df.isnull().sum())
df["pollutant_avg"]=df["pollutant_avg"].fillna(df["pollutant_avg"].mean())
df["pollutant_min"]=df["pollutant_min"].fillna(df["pollutant_min"].mean())
df["pollutant_max"]=df["pollutant_max"].fillna(df["pollutant_max"].mean())
#changing format
df['last_update'] = pd.to_datetime(df['last_update'],errors='coerce', format="%d-%m-%Y %H:%M:%S")

#removing duplicates
df.drop_duplicates()
#renaming columns
df.rename(columns={
    "pollutant_min": "min_pollution",
    "pollutant_max": "max_pollution",
    "pollutant_avg": "avg_pollution"},inplace=True)

print("CLEANED DATA:\n",df.isnull().sum())
print(df.head(10).to_string())
df.to_csv("CLEANED.csv")