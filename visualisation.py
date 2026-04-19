import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('master_dataset.csv')

# Add tercile column
df['tercile'] = pd.qcut(df['carbon_intensity'], q=3, labels=['Low', 'Mid', 'High'])

# CHART 1: Average annual return by tercile
tercile_summary = df.groupby('tercile', observed=False)[['annual_return_2022', 'return_on_equity']].mean()

fig, ax = plt.subplots(figsize=(8, 6))

colors = ['#2ecc71', '#f39c12', '#e74c3c']
bars = ax.bar(tercile_summary.index, tercile_summary['annual_return_2022'], color=colors, edgecolor='white', width=0.5)

# Add value labels on bars
for bar, val in zip(bars, tercile_summary['annual_return_2022']):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.002,
            f'{val:.1%}', ha='center', va='bottom', fontsize=11, fontweight='bold')

ax.set_xlabel('Carbon Intensity Tercile', fontsize=12)
ax.set_ylabel('Average Annual Stock Return 2022', fontsize=12)
ax.set_title('Average Stock Return by Carbon Intensity Tercile\n(Global Utilities, 2022)', fontsize=13)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.0%}'))
ax.axhline(y=0, color='black', linewidth=0.8, linestyle='--', alpha=0.5)
ax.set_ylim(-0.05, 0.06)

plt.tight_layout()
plt.savefig('chart_tercile_returns.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart 1 saved")

# CHART 2: Correlation heatmap
import seaborn as sns

corr_cols = ['carbon_intensity', 'annual_return_2022', 'return_on_equity']
corr_matrix = df[corr_cols].corr()

# Rename columns for cleaner labels
corr_matrix.columns = ['Carbon Intensity', 'Annual Return', 'Return on Equity']
corr_matrix.index = ['Carbon Intensity', 'Annual Return', 'Return on Equity']

fig, ax = plt.subplots(figsize=(8, 6))

sns.heatmap(corr_matrix, 
            annot=True, 
            fmt='.2f', 
            cmap='RdYlGn',
            center=0,
            vmin=-1, vmax=1,
            ax=ax,
            linewidths=0.5,
            annot_kws={'size': 11})

ax.set_title('Correlation Matrix: Carbon Intensity vs Financial Metrics\n(Global Utilities, 2022)', fontsize=13)

plt.tight_layout()
plt.savefig('chart_correlation_heatmap.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart 2 saved")