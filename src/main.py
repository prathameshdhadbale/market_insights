from fetch_data import fetch_stock_data
from analysis import calculate_metrics
from visualize import plot_stock_prices


def main():
    tickers = ["AAPL", "MSFT", "TSLA" , "GOOGL"]

    data = {}
    results = {}

    for ticker in tickers:
        df = fetch_stock_data(ticker)
        data[ticker] = df
        results[ticker] = calculate_metrics(df)

    print("\n Stock Comparison\n")

    for stock, metrics in results.items():
        print(f"{stock}")
        print(f"   Trend: {metrics['trend'] * 100:.2f}%")
        print(f"   Volatility: {metrics['volatility'] * 100:.2f}%\n")

    plot_stock_prices(data)


if __name__ == "__main__":
    main()
