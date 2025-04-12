#Assess Pollutant Variability in Major Cities
import numpy as nm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("CLEANED.csv")
# Filter for PM2.5 and NO2 in major cities
major_cities = ['Delhi', 'Bengaluru', 'Hyderabad']
pollutant_data = df[(df['pollutant_id'].isin(['PM2.5', 'NO2'])) & (df['city'].isin(major_cities))]
pivot_data = pollutant_data.pivot_table(values='avg_pollution', index=['city', 'station'], columns='pollutant_id').reset_index()

sns.pairplot(pivot_data, hue='city', vars=['PM2.5', 'NO2'], palette='deep')
plt.suptitle('PM2.5 vs. NO2 in Major Cities', y=1.02)
plt.savefig('pollutant_city_pair.png')
plt.show()