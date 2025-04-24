#Assess Pollutant Hotspots Using Geospatial Visualization
#made by ANISHA 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("CLEANED.csv")
pm25_data = df[df['pollutant_id'] == 'PM2.5']
fig, ax = plt.subplots(figsize=(10, 8))
scatter = sns.scatterplot(data=pm25_data, x='longitude', y='latitude', size='avg_pollution', hue='avg_pollution', palette='nipy_spectral', sizes=(50, 500), alpha=0.6, legend=False, ax=ax)
norm = plt.Normalize(pm25_data['avg_pollution'].min(), pm25_data['avg_pollution'].max())
sm = plt.cm.ScalarMappable(cmap='nipy_spectral', norm=norm)
fig.colorbar(sm, ax=ax, label='Average PM2.5 (µg/m³)')
ax.set_title('Geospatial Distribution of PM2.5 Levels Across India', fontsize=14, pad=10)
ax.set_xlabel('Longitude', fontsize=12)
ax.set_ylabel('Latitude', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
india_outline = [(68, 8), (68, 23), (74, 35), (80, 35), (88, 28), (97, 28), (97, 20), (92, 10), (80, 5), (68, 8)]
x, y = zip(*india_outline)
ax.plot(x, y, color='black', linewidth=1, linestyle='-', alpha=0.3)
plt.tight_layout()
plt.savefig('Geospatial Visualization.png')
plt.show()
