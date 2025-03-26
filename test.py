from fredapi import Fred
from config import FRED_API_KEY
import pandas as pd

fred = Fred(api_key=FRED_API_KEY)
series = fred.get_series("DGS10")  # 10-Year Treasury

# Display first few rows and index type
print(series.head())
print("\nSeries index type:", type(series.index[0]))

# Check available dates
print("\nClosest date to 2022-11-01:", series.loc["2022-11-01"])

# Print index to verify formatting
print("\nAvailable index sample:", series.index[:10])