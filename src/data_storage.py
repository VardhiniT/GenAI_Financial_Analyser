import yfinance as yf
import pandas as pd
import os

def update_stock_data(ticker="MSFT"):
    stock = yf.Ticker(ticker)

    # Get 5 years data
    new_data = stock.history(period="5y")

    file_path = f"data/{ticker}.csv"

    # Create data folder if not exists
    os.makedirs("data", exist_ok=True)

    # If file exists → append
    if os.path.exists(file_path):
        old_data = pd.read_csv(file_path, index_col=0)
        updated = pd.concat([old_data, new_data]).drop_duplicates()
    else:
        updated = new_data

    # Save
    updated.to_csv(file_path)

    return updated