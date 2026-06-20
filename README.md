# Natural Gas Price Forecasting (Time Series Analysis)

## 📌 Project Overview
This project analyzes historical natural gas prices from 2020 to 2024 and builds a simple forecasting model to estimate prices for any given date, including short-term future extrapolation.

The goal is to demonstrate practical data analysis skills, time-series understanding, and the ability to transform raw market data into actionable insights using Python.

---

## 💡 Business Context
Natural gas is a highly volatile commodity influenced by supply-demand dynamics, seasonal consumption, and macroeconomic conditions.

Accurate price estimation is important for:
- Energy trading and pricing strategies
- Long-term storage contract planning
- Financial risk assessment
- Market trend evaluation

This project provides a simplified approach to understanding price behaviour using historical patterns.

---

## 📁 Dataset
- Monthly natural gas price data
- Time period: October 2020 – September 2024
- Each data point represents end-of-month market prices from a time series snapshot

---

## ⚙️ Methodology

### 1. Data Preparation
- Loaded dataset using Pandas
- Converted date column into datetime format
- Sorted data in chronological order

### 2. Feature Engineering
- Converted dates into numerical format using ordinal encoding
- Enabled mathematical operations on time-series data

### 3. Modeling Approach
- Applied linear interpolation using SciPy (`interp1d`)
- Enabled extrapolation to estimate future values beyond available data

### 4. Forecasting Function
- Built reusable function `estimate_price(date)`
- Supports both historical lookup and future price estimation

---

## 📊 Key Insights
- Natural gas prices exhibit relatively smooth month-to-month transitions
- This makes interpolation a reasonable baseline approach for short-term estimation
- The model captures general trends but not abrupt market shocks

---

## ⚠️ Limitations
- Does not incorporate external factors (weather, geopolitical events, supply disruptions)
- Assumes linear transitions between data points
- Not suitable for long-term forecasting or high-volatility scenarios

---

## 🔮 Future Improvements
- Implement advanced forecasting models (ARIMA / Prophet)
- Add seasonality decomposition analysis
- Compare multiple models for performance evaluation
- Build interactive dashboard (Streamlit / Power BI)

---

## 🧰 Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib
- SciPy

---

## 📈 Features
- Estimate natural gas price for any date
- Historical trend visualization
- Future price extrapolation (12-month forecast)
- Simple and interpretable time-series model

---

## 🚀 How to Run

```bash
git clone https://github.com/your-username/natural-gas-price-forecast.git
cd natural-gas-price-forecast
