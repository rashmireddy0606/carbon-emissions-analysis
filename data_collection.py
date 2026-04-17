import yfinance as yf
import pandas as pd

# Load emissions data
emissions_df = pd.read_csv('emissions_data_with_tickers.csv')
print(f"Loaded {len(emissions_df)} companies from emissions data")
print()

results = []

for _, row in emissions_df.iterrows():
    ticker = row['yfinance_ticker']
    company = row['company']
    
    try:
        stock = yf.Ticker(ticker)
        
        # Pull annual income statement
        financials = stock.financials
        
        # yfinance returns columns as dates - find the 2022 column
        cols_2022 = [col for col in financials.columns if '2022' in str(col)]
        
        if cols_2022:
            col = cols_2022[0]
            revenue = financials.loc['Total Revenue', col] if 'Total Revenue' in financials.index else None
            
            # Pull other metrics
            info = stock.info
            market_cap = info.get('marketCap')
            roe = info.get('returnOnEquity')
            
            # Pull 2022 annual stock return separately
            hist = stock.history(start='2022-01-01', end='2022-12-31')
            if not hist.empty:
                start_price = hist['Close'].iloc[0]
                end_price = hist['Close'].iloc[-1]
                annual_return = (end_price - start_price) / start_price
            else:
                annual_return = None
                
            results.append({
                'ticker': ticker,
                'company': company,
                'revenue_2022': revenue,
                'market_cap': market_cap,
                'return_on_equity': roe,
                'annual_return_2022': annual_return,
                'status': 'OK' if revenue is not None else 'MISSING DATA'
            })
            print(f"✓ {company} ({ticker}) — 2022 revenue: {revenue}")
            
        else:
            results.append({
                'ticker': ticker,
                'company': company,
                'revenue_2022': None,
                'market_cap': None,
                'return_on_equity': None,
                'annual_return_2022': None,
                'status': 'NO 2022 DATA'
            })
            print(f"✗ {company} ({ticker}) — no 2022 financials found")
            
    except Exception as e:
        results.append({
            'ticker': ticker,
            'company': company,
            'revenue_2022': None,
            'market_cap': None,
            'return_on_equity': None,
            'annual_return_2022': None,
            'status': f'ERROR: {e}'
        })
        print(f"✗ {company} ({ticker}) — {e}")

# Save results
results_df = pd.DataFrame(results)
results_df.to_csv('financial_data_2022.csv', index=False)
print()
print("--- SUMMARY ---")
print(results_df[['company', 'ticker', 'revenue_2022', 'annual_return_2022', 'status']])