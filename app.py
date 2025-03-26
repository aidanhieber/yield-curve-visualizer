import streamlit as st
import pandas as pd
from datetime import date
from data_loader import get_yield_curve_data
import plotly.express as px  # Added for custom plotting

# --- Page Title ---
st.title("📈 U.S. Treasury Yield Curve Visualizer")
st.caption("Select a date to view the historical yield curve from the FRED database.")

# --- Date Picker ---
selected_date = st.date_input("Pick a date", value=date.today())

# --- Fetch Data ---
st.write("Fetching data for:", selected_date)
curve, actual_date_used = get_yield_curve_data(selected_date)
curve = curve.dropna()

if not curve.empty:
    st.write(f"### Yield Curve (Data from {actual_date_used})")
    st.write(curve)

    # Define correct order of maturities
    ordered_maturities = ["1M", "3M", "6M", "1Y", "2Y", "3Y", "5Y", "7Y", "10Y", "20Y", "30Y"]

    # Prepare and reorder DataFrame
    df = pd.DataFrame({
        "Maturity": curve.index,
        "Yield": curve.values
    })
    df = df[df["Maturity"].isin(ordered_maturities)]
    df["Maturity"] = pd.Categorical(df["Maturity"], categories=ordered_maturities, ordered=True)
    df = df.sort_values("Maturity")

    # Plot with Plotly
    fig = px.line(
        df,
        x="Maturity",
        y="Yield",
        title=f"US Treasury Yield Curve ({actual_date_used})",
        markers=True
    )
    fig.update_layout(
        xaxis_title="Maturity",
        yaxis_title="Yield (%)",
        height=500
    )
    st.plotly_chart(fig)

    # Show slope insight
    if "10Y" in curve and "2Y" in curve:
        slope = curve["10Y"] - curve["2Y"]
        st.write(f"**10Y–2Y Slope:** {slope:.2f}%")
        if slope < 0:
            st.warning("Yield curve is inverted!")
        elif slope < 0.5:
            st.info("Curve is flat or slightly upward sloping.")
        else:
            st.success("Steep, upward-sloping curve.")
else:
    st.error("⚠️ No yield data found for this date.")

