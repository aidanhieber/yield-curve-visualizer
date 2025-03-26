from data_loader import get_yield_curve_data
from plot_yield_curve import plot_yield_curve
from datetime import datetime

# Optional: specify a date like '2022-3-15'
target_date = "2024-12-24"

curve = get_yield_curve_data(target_date)
curve = curve.dropna()
if not curve.empty:
    plot_yield_curve(curve, target_date)
else:
    print("[!] No valid data available for that date.")