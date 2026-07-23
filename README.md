# 🌍 Global Air Quality Data Analysis

A Python-based exploratory data analysis (EDA) project that studies global air quality patterns using AQI (Air Quality Index), PM2.5, temperature, and humidity data collected across major cities worldwide.

---

## 📌 Project Overview

This project loads a global air quality dataset and performs data cleaning, datetime feature engineering, and visual exploratory analysis to uncover trends and relationships in air pollution data across different cities and time periods.

## 📂 Dataset

- **File:** `globalAirQuality.csv`
- **Size:** 18,000 rows × 19 columns
- **Coverage:** Multiple countries and cities (e.g., New York, Zurich, London, Tokyo, Dubai, and more)
- **Key columns:** `timestamp`, `country`, `city`, `latitude`, `longitude`, `aqi`, `pm25`, `temperature`, `humidity`

## ⚙️ What This Project Does

1. **Data Loading & Cleaning** — Loads the CSV, creates a working copy, and validates fields (e.g., checking for negative humidity values).
2. **Feature Engineering** — Converts `timestamp` to datetime and extracts `year`, `month`, `day`, and `hour` for time-based analysis.
3. **Exploratory Visualizations** — Generates five key charts to understand air quality patterns.

## 📊 Visualizations

| # | Chart Type | Insight |
|---|-----------|---------|
| 1 | Line Chart | AQI trend over time across all recorded timestamps |
| 2 | Histogram | Frequency distribution of AQI values |
| 3 | Scatter Plot | Relationship between temperature and humidity |
| 4 | Bar Chart | Average AQI comparison across all cities |
| 5 | Box Plot | Spread and outliers of PM2.5 levels across cities |

## 🛠️ Tech Stack

- **Python 3**
- **Pandas** — data manipulation
- **NumPy** — numerical operations
- **Matplotlib** — data visualization

## ▶️ How to Run

```bash
pip install pandas numpy matplotlib
python freelance.py
```

Make sure `globalAirQuality.csv` is in the same directory as `freelance.py`.

## 📈 Sample Output

Running the script displays five separate figure windows:
- AQI Trend Over Time
- AQI Distribution Histogram
- Temperature vs Humidity Scatter Plot
- Average AQI by City Bar Chart
- PM2.5 Spread by City Box Plot

*(Tip: add `plt.savefig('filename.png')` before each `plt.show()` if you want to save these charts as image files for a portfolio or report.)*

## 👤 Author

**Muhammad Bilal Ifzal**
- GitHub: [github.com/bilalifzal](https://github.com/bilalifzal)
- LinkedIn: [linkedin.com/in/muhammad-bilal-ifzal-a82649375](https://linkedin.com/in/muhammad-bilal-ifzal-a82649375)
- Portfolio: [muhammad-bilal-ifzal-portfolio.lovestoblog.com](https://muhammad-bilal-ifzal-portfolio.lovestoblog.com)

---

*This project is part of ongoing practice in data analysis and visualization using Python.*
