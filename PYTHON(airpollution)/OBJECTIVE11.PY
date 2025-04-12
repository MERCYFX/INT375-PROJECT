#Explore PM10 vs. PM2.5 Ratios Across States
import numpy as nm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("CLEANED.csv")
pm_data = df[df['pollutant_id'].isin(['PM2.5', 'PM10'])].pivot_table(index=['state', 'station'], columns='pollutant_id', values='avg_pollution').dropna()
pm_data['ratio'] = pm_data['PM10'] / pm_data['PM2.5']
ratio_by_state = pm_data.groupby('state')['ratio'].mean().reset_index()
sns.barplot(data=ratio_by_state, x='ratio', y='state',color="m")
plt.title('Average PM10/PM2.5 Ratio by State')
plt.xlabel('PM10/PM2.5 Ratio')
plt.ylabel('State')
plt.savefig('PM10 vs. PM2.5 Ratios.png')
plt.show()