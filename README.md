# Natural Gas Price Forecasting (Time Series Analysis)

## 📌 Overview
This project analyzes historical natural gas prices from 2020 to 2024 and builds a simple forecasting model to estimate prices for any given date, including short-term future extrapolation.

The objective is to demonstrate data analysis skills, time-series understanding, and basic predictive modeling using Python.

---

## 📊 Business Context
Natural gas prices fluctuate over time due to market demand, supply conditions, and external economic factors. Accurate price estimation is useful for:

- Energy trading decisions
- Long-term storage contract planning
- Financial risk assessment
- Market trend analysis

---

## 📁 Dataset
- Monthly natural gas price data
- Time period: October 2020 – September 2024
- Data represents end-of-month market prices from a time series snapshot

---

## ⚙️ Methodology

### 1. Data Preparation
- Loaded dataset using Pandas
- Converted date column to datetime format
- Sorted data chronologically

### 2. Feature Engineering
- Converted dates into numerical format using ordinal encoding
- Enabled mathematical processing of time-series data

### 3. Modeling Approach
- Applied linear interpolation using SciPy (`interp1d`)
- Enabled extrapolation for future price estimation

### 4. Forecasting Function
- Built reusable function `estimate_price(date)`
- Supports both historical lookup and future prediction

---

## 📈 Key Features
- Estimate natural gas price for any given date
- Handle both historical and future date prediction
- Visualize historical trends and forecasted values
- Simple and interpretable time-series model

---

## 🧰 Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib
- SciPy

---

## 🚀 How to Run

### 1. Clone repository
```bash
git clone https://github.com/your-username/natural-gas-price-forecast.git
cd natural-gas-price-forecast
