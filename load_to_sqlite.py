import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load CSV files
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/processed/02_nav_history_cleaned.csv")
scheme_performance = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")
investor_transactions = pd.read_csv("data/processed/08_investor_transactions_cleaned.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

# Load tables into SQLite
fund_master.to_sql("dim_fund", engine, if_exists="replace", index=False)

nav_history.to_sql("fact_nav", engine, if_exists="replace", index=False)

scheme_performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

investor_transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

# Verify row counts
print("dim_fund:", len(fund_master))
print("fact_nav:", len(nav_history))
print("fact_performance:", len(scheme_performance))
print("fact_transactions:", len(investor_transactions))
print("fact_aum:", len(aum))

print("\nDatabase loaded successfully!")