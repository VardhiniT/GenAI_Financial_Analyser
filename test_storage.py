from src.data_storage import update_stock_data
from src.analytics import compute_metrics, format_metrics

df = update_stock_data("MSFT")

metrics = compute_metrics(df)

print(format_metrics("MSFT", metrics))