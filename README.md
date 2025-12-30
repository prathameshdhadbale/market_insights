#  Market Insights – Stock Analysis Tool

A lightweight Python application that analyzes stock market data using **Yahoo Finance**.
It calculates key financial metrics and visualizes price movements to help understand market behavior.

This project focuses on **clean architecture, clarity, and real-world data handling**.

---

##  Features

* Fetches real-time historical stock data using `yfinance`
* Calculates:

  * **Trend** (overall price movement)
  * **Volatility** (price fluctuation)
* Compares multiple stocks side by side
* Visualizes price movement using line charts
* Clean, modular, and readable codebase

---

##  What This Project Demonstrates

* Working with real-world financial APIs
* Cleaning and structuring raw market data
* Applying basic quantitative analysis
* Writing modular, maintainable Python code
* Designing small systems with clear responsibilities

This project prioritizes **correctness, clarity, and structure** over unnecessary complexity.

---

##  Tech Stack

* **Python 3**
* **pandas** – data processing
* **yfinance** – stock market data
* **matplotlib** – data visualization

---

##  Project Structure

```
market_insights/
│
├── src/
│   ├── main.py           # Entry point
│   ├── fetch_data.py     # Data fetching logic
│   ├── analysis.py       # Financial calculations
│   └── visualize.py      # Plotting logic
│
├── tests/
│   └── test_analysis.py  # Basic test structure
│
├── requirements.txt
└── README.md
```

---

##  How to Run

### 1. Clone the repository

```bash
git clone https://github.com/prathameshdhadbale/market_insights.git
cd market_insights
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python src/main.py
```

---

##  Example Output

```
 Stock Comparison

AAPL
   Trend: -3.30%
   Volatility: 0.70%

MSFT
   Trend: 1.42%
   Volatility: 0.55%
```

A graph window will also open showing price movements over time.

---

##  How It Works

1. **Data Fetching**
   Uses `yfinance` to retrieve historical stock prices.

2. **Data Cleaning**
   Handles multi-level columns and ensures consistent formatting.

3. **Analysis**

   * Trend = percentage price change over time
   * Volatility = standard deviation of daily returns

4. **Visualization**

   * Line plots for easy comparison of stock performance.

---

##  Possible Improvements

* Command-line arguments for dynamic ticker input
* Export analysis results to CSV
* Add moving averages or indicators
* Add automated tests
* Support longer time ranges

---

##  Why I Built This

I built this project to understand how real-world financial data can be transformed into meaningful insights using clean, maintainable Python code.
The focus was on **clarity, correctness, and good software design practices**.

---

##  Final Notes

This project demonstrates my approach to:

* Problem-solving
* Code organization
* Data-driven thinking

It is intentionally simple, readable, and extensible.
