import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Load data
df = pd.read_csv("data/Nat_Gas.csv")

# Convert date
df["Dates"] = pd.to_datetime(df["Dates"])
df = df.sort_values("Dates")

# Convert date to numeric scale
x = df["Dates"].map(pd.Timestamp.toordinal)
y = df["Prices"]

# Interpolation model
price_model = interp1d(x, y, kind="linear", fill_value="extrapolate")

# Function to estimate price
def estimate_price(date):
    date = pd.to_datetime(date)
    return float(price_model(date.toordinal()))

# Test examples
if __name__ == "__main__":
    print("Historical Estimate:", estimate_price("2023-06-15"))
    print("Future Estimate:", estimate_price("2025-06-30"))

    # Future forecasting (1 year)
    future_dates = pd.date_range(
        start=df["Dates"].max(),
        periods=13,
        freq="ME"
    )

    future_prices = [estimate_price(d) for d in future_dates]

    # Plot
    plt.figure(figsize=(12,5))

    plt.plot(df["Dates"], df["Prices"], label="Historical")
    plt.plot(future_dates, future_prices, "--", label="Forecast")

    plt.title("Natural Gas Price Forecast")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)

    plt.show()
"""