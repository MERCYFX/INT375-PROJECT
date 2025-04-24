#Visualize Pollutant Composition by State
#made by ANISHA
import numpy as nm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("CLEANED.csv")
# Pivot data for pollutant composition
pivot_df = df.pivot_table(values='avg_pollution', index='state', columns='pollutant_id', aggfunc='mean').dropna()

plt.figure(figsize=(12, 8))
sns.set_style('whitegrid')
pivot_df.plot(kind='bar', stacked=True, colormap='tab20')
plt.title('Pollutant Composition by State')
plt.xlabel('State')
plt.ylabel('Average Concentration (µg/m³)')
plt.xticks(rotation=90)
plt.legend(title='Pollutant')
plt.tight_layout()
plt.savefig('pollutant_state_stacked.png')
plt.show()
