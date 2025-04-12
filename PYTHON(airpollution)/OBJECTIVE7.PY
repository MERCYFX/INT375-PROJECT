#Explore SO2 Levels by Region
import numpy as nm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("UNCLEANED.csv")
# Filter SO2 data
so2_data = df[df['pollutant_id'] == 'SO2']
plt.figure(figsize=(12, 8))
sns.stripplot(x='state', y='pollutant_avg', data=so2_data, palette='bright', size=4)
plt.title('SO2 Levels by State')
plt.xlabel('State')
plt.ylabel('SO2 Concentration (µg/m³)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('so2_state_strip.png')
plt.show()