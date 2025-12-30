import matplotlib.pyplot as plt


def plot_stock_prices(data_dict):
    """
    Plot closing prices for multiple stocks.

    data_dict: {
        "AAPL": DataFrame,
        "MSFT": DataFrame,
        ...
    }
    """

    for ticker, df in data_dict.items():
        plt.plot(df.index, df["Close"], label=ticker)

    plt.title("Stock Price Comparison")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)

    plt.show()
