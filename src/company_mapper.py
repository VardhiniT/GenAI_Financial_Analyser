def get_ticker_from_query(query):

    query = query.lower()

    mapping = {
        "microsoft": "MSFT",
        "apple": "AAPL",
        "tesla": "TSLA",
        "google": "GOOGL",
        "amazon": "AMZN",
        "nvidia": "NVDA",
        "meta": "META"
    }

    found = []

    for name, ticker in mapping.items():
        if name in query:
            found.append(ticker)

    return found