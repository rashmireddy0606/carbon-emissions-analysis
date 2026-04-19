import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('master_dataset.csv')

print(f"Loaded {len(df)} companies")
print(df[['company', 'carbon_intensity', 'annual_return_2022']].head())

# Calculate regression line
slope, intercept, r_value, p_value, std_err = stats.linregress(
    df['carbon_intensity'], 
    df['annual_return_2022']
)

# Create scatter plot
fig, ax = plt.subplots(figsize=(12, 8))

ax.scatter(df['carbon_intensity'], df['annual_return_2022'], 
           color='steelblue', alpha=0.7, s=100, zorder=5)

# Add regression line
x_line = np.linspace(df['carbon_intensity'].min(), df['carbon_intensity'].max(), 100)
y_line = slope * x_line + intercept
ax.plot(x_line, y_line, color='red', linewidth=2, label=f'R² = {r_value**2:.3f}, p = {p_value:.3f}')

# Label each company dot
for _, row in df.iterrows():
    ax.annotate(row['company'], 
                (row['carbon_intensity'], row['annual_return_2022']),
                fontsize=7, alpha=0.8,
                xytext=(5, 5), textcoords='offset points')

# Labels and formatting
ax.set_xlabel('Carbon Intensity (tCO₂ / USD Revenue)', fontsize=12)
ax.set_ylabel('Annual Stock Return 2022', fontsize=12)
ax.set_title('Carbon Intensity vs. Annual Stock Return (Global Utilities, 2022)', fontsize=14)
ax.legend(fontsize=11)
ax.axhline(y=0, color='black', linewidth=0.8, linestyle='--', alpha=0.5)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.0%}'))
ax.set_xscale('log')

plt.tight_layout()
plt.savefig('scatter_carbon_vs_return.png', dpi=150, bbox_inches='tight')
plt.show()
print("Scatter plot saved")

# --- TERCILE ANALYSIS ---
df['tercile'] = pd.qcut(df['carbon_intensity'], q=3, labels=['Low', 'Mid', 'High'])

tercile_summary = df.groupby('tercile')[['annual_return_2022', 'return_on_equity']].mean()
print("\n--- TERCILE ANALYSIS ---")
print(tercile_summary)

# Correlation metrics
metrics = {
    'Annual Return': 'annual_return_2022',
    'Return on Equity': 'return_on_equity'
}

print("\n--- CARBON INTENSITY CORRELATIONS ---")
for label, col in metrics.items():
    clean = df[['carbon_intensity', col]].dropna()
    r, p = stats.pearsonr(clean['carbon_intensity'], clean[col])
    print(f"{label}: r = {r:.3f}, p = {p:.3f}")


# --- SUMMARY ---
print("\n--- FULL SUMMARY ---")
print(f"Sample size: {len(df)} companies")
print(f"Pearson R² = {r_value**2:.3f}, p = {p_value:.3f}")
print(f"Pearson correlation = {r_value:.3f}")