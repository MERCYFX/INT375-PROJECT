#Study Ozone Levels Across States
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("CLEANED.csv")
# Filter ozone data
ozone_data = df[df['pollutant_id'] == 'OZONE']
plt.figure(figsize=(12, 8))
sns.violinplot(x='state', y='avg_pollution', data=ozone_data.head(1000), palette='muted')  # Limited for clarity
plt.title('Ozone Levels by State')
plt.xlabel('State')
plt.ylabel('Ozone Concentration (µg/m³)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('ozone_state_violin.png')
plt.show()