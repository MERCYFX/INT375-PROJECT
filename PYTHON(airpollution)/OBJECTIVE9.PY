#Analyze Pollutant Trends by Latitude
#MADE BY ANISHA
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("CLEANED.csv")
# Filter PM2.5 data
pm25_data = df[df['pollutant_id'] == 'PM2.5']

# Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='latitude', y='avg_pollution', data=pm25_data, hue='avg_pollution', palette='viridis', size='avg_pollution')
plt.title('PM2.5 Levels vs. Latitude')
plt.xlabel('Latitude')
plt.ylabel('PM2.5 Concentration (µg/m³)')
plt.tight_layout()
plt.savefig('pm25_latitude_scatter.png')
plt.show()
