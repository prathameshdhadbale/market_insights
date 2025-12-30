import pandas as pd
from src.analysis import calculate_metrics


def test_calculate_metrics_output():
    # Sample stock data
    data = {
        "Close": [100, 102, 101, 105, 110]
    }

    df = pd.DataFrame(data)

    result = calculate_metrics(df)

    # Check expected keys
    assert "trend" in result
    assert "volatility" in result

    # Check value types
    assert isinstance(result["trend"], float)
    assert isinstance(result["volatility"], float)
