

def calculate_metrics(df):

    daily_return = df["Close"].pct_change() 
    volatility = daily_return.std() 
    trend = (df["Close"].iloc[-1] - df["Close"].iloc[0])/(df["Close"].iloc[0])

    return {
        "volatility" : float(volatility),
        "trend" : float(trend)
    }