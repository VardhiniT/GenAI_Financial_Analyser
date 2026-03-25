import pandas as pd

def compute_metrics(df):
    df = df.dropna()

    # Daily returns
    df["Returns"] = df["Close"].pct_change()

    # 1-year growth (approx 252 trading days)
    growth_1y = (df["Close"].iloc[-1] - df["Close"].iloc[-252]) / df["Close"].iloc[-252]

    # 5-year growth
    growth_5y = (df["Close"].iloc[-1] - df["Close"].iloc[0]) / df["Close"].iloc[0]

    # Volatility (risk)
    volatility = df["Returns"].std()

    # Average return
    avg_return = df["Returns"].mean()

    return {
        "growth_1y": growth_1y,
        "growth_5y": growth_5y,
        "volatility": volatility,
        "avg_return": avg_return
    }


def format_metrics(ticker, metrics):
    return f"""
    {ticker} Financial Analysis:

    1-Year Growth: {metrics['growth_1y']*100:.2f}%
    5-Year Growth: {metrics['growth_5y']*100:.2f}%
    Volatility (Risk): {metrics['volatility']:.4f}
    Average Daily Return: {metrics['avg_return']:.4f}
    """

def compare_companies(df1, df2, t1="Company1", t2="Company2"):

    m1 = compute_metrics(df1)
    m2 = compute_metrics(df2)

    return f"""
    Comparison Analysis:

    {t1} vs {t2}

    1-Year Growth: {m1['growth_1y']*100:.2f}% vs {m2['growth_1y']*100:.2f}%
    5-Year Growth: {m1['growth_5y']*100:.2f}% vs {m2['growth_5y']*100:.2f}%

    Volatility: {m1['volatility']:.4f} vs {m2['volatility']:.4f}
    Average Return: {m1['avg_return']:.4f} vs {m2['avg_return']:.4f}
    """