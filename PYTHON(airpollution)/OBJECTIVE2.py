#Analyze the Distribution of PM2.5 Levels Across India
#made by ANISHA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("CLEANED.csv")
pm25_data = df[df['pollutant_id'] == 'PM2.5']
sns.set_style('whitegrid')
plt.figure(figsize=(10, 6))
sns.histplot(pm25_data['avg_pollution'], bins=30, kde=True, color='blue')
plt.title('Distribution of PM2.5 Levels Across India')
plt.xlabel('PM2.5 Concentration (µg/m³)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('pm25_distribution.png')
plt.show()
