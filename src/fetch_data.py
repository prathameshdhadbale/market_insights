import yfinance as yf
import pandas as pd


def fetch_stock_data(ticker: str, period: str = "1mo") -> pd.DataFrame:
    """
    Fetch historical stock data for a given ticker.
    """

    data = yf.download(ticker, period=period)

    if data.empty:
        raise ValueError(f"No data found for ticker: {ticker}")

    # Extract correct ticker level (robust solution)
    if isinstance(data.columns, pd.MultiIndex):
        data = data.xs(ticker, axis=1, level=1)

    data.columns.name = None

    return data
