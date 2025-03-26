from fredapi import Fred
from config import FRED_API_KEY
import pandas as pd

def get_yield_curve_data(date=None):
    fred = Fred(api_key=FRED_API_KEY)

    maturities = {
        "1M": "DGS1MO",
        "3M": "DGS3MO",
        "6M": "DGS6MO",
        "1Y": "DGS1",
        "2Y": "DGS2",
        "3Y": "DGS3",
        "5Y": "DGS5",
        "7Y": "DGS7",
        "10Y": "DGS10",
        "20Y": "DGS20",
        "30Y": "DGS30"
    }

    data = {}
    actual_date = None  # <-- initialize here

    for label, code in maturities.items():
        series = fred.get_series(code)

        try:
            if date:
                date = pd.to_datetime(date)
                valid_series = series.loc[:date].dropna()
                value = valid_series.iloc[-1]

                # Set the actual_date the first time we get valid data
                if actual_date is None:
                    actual_date = valid_series.index[-1]
            else:
                valid_series = series.dropna()
                value = valid_series.iloc[-1]
                if actual_date is None:
                    actual_date = valid_series.index[-1]

            data[label] = value
        except Exception as e:
            print(f"[!] Error fetching {label} on {date}: {e}")
            data[label] = None

    return pd.Series(data, name="Yield (%)"), actual_date.date() if actual_date else None
