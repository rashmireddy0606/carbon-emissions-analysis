import pandas as pd
import numpy as np

emissions_df = pd.read_csv('emissions_data_with_tickers.csv')

financial_df = pd.read_csv('financial_data_2022.csv')

print("Emissions data shape:", emissions_df.shape)
print("Financial data shape:", financial_df.shape)
print()
print(emissions_df.head())
print()
print(financial_df.head())

financial_df = financial_df.rename(columns={'ticker': 'yfinance_ticker'})

merged_df = pd.merge(emissions_df, financial_df, on='yfinance_ticker', how='inner')

merged_df = merged_df.dropna(subset=['revenue_2022'])

print(f"Merged dataset: {len(merged_df)} companies")
print(merged_df.head())

merged_df['carbon_intensity'] = merged_df['scope1_emissions_tco2'] / merged_df['revenue_2022']
print("Carbon intensity calculated")
print()
print(merged_df[['company_x', 'scope1_emissions_tco2', 'revenue_2022', 'carbon_intensity']].sort_values('carbon_intensity', ascending=False))
merged_df = merged_df.rename(columns={'company_x': 'company'})
merged_df = merged_df.drop(columns=['company_y'])

merged_df.to_csv('master_dataset.csv', index=False)
print()
print(f"Master dataset saved with {len(merged_df)} companies and {len(merged_df.columns)} columns")
print("Columns:", list(merged_df.columns))