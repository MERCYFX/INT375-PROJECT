#Compare Average PM2.5 Levels by State
#MADE BY ANISHA KUMARI
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("CLEANED.csv")
# Filter and group PM2.5 data by state
pm25_state_avg = df[df['pollutant_id'] == 'PM2.5'].groupby('state')['avg_pollution'].mean().sort_values(ascending=False).reset_index()

# Plot
plt.figure(figsize=(12, 8))
sns.barplot(x='avg_pollution', y='state', data=pm25_state_avg.head(10), palette='viridis')
plt.title('Top 10 States by Average PM2.5 Levels')
plt.xlabel('Average PM2.5 (µg/m³)')
plt.ylabel('State')
plt.tight_layout()
plt.savefig('pm25_state_bar.png')
plt.show()
