# Carbon Emissions vs. Financial Performance: A Utilities Sector Analysis

## Research Question
Is there a statistically significant association between carbon intensity and financial performance among listed utility companies?

## Data Sources
- **Sample Frame:** iShares Global Utilities ETF (JXI), as of April 2026
- **Emissions Data:** Scope 1 GHG emissions sourced from NZDPU (nzdpu.com), reporting year 2022
- **Financial Data:** Revenue, stock returns, ROE, and market cap sourced via yfinance, year 2022

## Sampling Methodology
The sampling frame is all utility equity constituents of JXI as of April 2026. Companies were excluded only where 2022 financial data was unavailable via yfinance, resulting in a final analytical sample of 45 companies across 15 countries.

One company was excluded:
- Eletrobras (ELET3.SA) — unavailable 2022 financial data via yfinance

## Limitations
- Correlation analysis only — causation cannot be inferred due to confounding variables including regulatory environment, geography, and energy policy
- Market cap reflects current values (2025/2026) rather than 2022 figures due to yfinance data constraints
- Emissions data is self-reported by companies via NZDPU and has not been independently verified
- Sample is limited to JXI constituents and may not represent the full global utilities universe

## Project Structure
- `data_collection.py` — fetches 2022 financial data from yfinance
- `data_preparation.py` — cleans, merges, and calculates carbon intensity
- `analysis.py` — correlation analysis and statistical tests
- `visualisation.py` — generates charts and figures

## Results
*To be completed*

## Further Work
*To be completed*