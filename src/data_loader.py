import yfinance as yf
import pandas as pd
from embeddings import create_embeddings
from vector_store import create_vector_store

def fetch_stock_data(ticker="MSFT"):
    stock = yf.Ticker(ticker)

    info = stock.info
    financials = stock.financials
    balance_sheet = stock.balance_sheet
    cashflow = stock.cashflow

    # Convert everything to text
    data_text = f"""
    COMPANY INFO:
    {info}

    FINANCIALS:
    {financials.to_string()}

    BALANCE SHEET:
    {balance_sheet.to_string()}

    CASH FLOW:
    {cashflow.to_string()}
    """

    df = pd.DataFrame([{"text": data_text}])

    print("\nDataFrame Shape:", df.shape)
    print("\nDataFrame Columns:", df.columns[:10])

    return df


if __name__ == "__main__":
    df = fetch_stock_data()

    print("\nSample Data:\n", df.head())

    texts, embeddings = create_embeddings(df)

    print("\n--- SAMPLE CHUNK ---")
    print(texts[0])

    print("\n STARTING VECTOR DB CREATION...")   # ADDED THIS
    vector_db = create_vector_store(texts, embeddings)