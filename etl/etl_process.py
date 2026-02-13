import pandas as pd
import sqlite3

# EXTRACT
df = pd.read_csv("data/sales_data.csv")
df.columns = df.columns.str.strip().str.lower()

# TRANSFORM
df = df.drop_duplicates()
df["amount"] = df["amount"].fillna(0).astype(int)
df["order_date"] = pd.to_datetime(df["order_date"])

def category(amount):
    if amount < 5000:
        return "Low"
    elif amount <= 10000:
        return "Medium"
    else:
        return "High"

df["amount_category"] = df["amount"].apply(category)

# LOAD
conn = sqlite3.connect("sales.db")
df.to_sql("sales_target", conn, if_exists="replace", index=False)

print("ETL Process Completed Successfully")
