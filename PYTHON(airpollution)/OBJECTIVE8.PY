#Investigate CO Levels in Urban vs. Rural Areas
#MADE by ANISHA
import numpy as nm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("UNCLEANED.csv")
# Filter CO data
co_data = df[df['pollutant_id'] == 'CO'].copy()

# Simple urban/rural classification (example)
urban_cities = ['Delhi', 'Bengaluru', 'Hyderabad', 'Chennai', 'Kolkata']
co_data['area_type'] = co_data['city'].apply(lambda x: 'Urban' if x in urban_cities else 'Rural')

plt.figure(figsize=(10, 6))
sns.swarmplot(x='area_type', y='pollutant_avg', data=co_data, palette='Set1')
plt.title('CO Levels in Urban vs. Rural Areas')
plt.xlabel('Area Type')
plt.ylabel('CO Concentration (µg/m³)')
plt.tight_layout()
plt.savefig('co_area_swarm.png')
plt.show()
