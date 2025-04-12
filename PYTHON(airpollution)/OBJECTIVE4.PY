#Examine Pollutant Correlations
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("CLEANED.csv")
# Pivot data for correlation
pivot_df = df.pivot_table(values='avg_pollution', index='station', columns='pollutant_id', aggfunc='mean')
pivot_df = pivot_df.dropna()

# Compute correlation
corr = pivot_df.corr()

# Plot
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Between Pollutants')
plt.tight_layout()
plt.savefig('pollutant_correlation_heatmap.png')
plt.show()