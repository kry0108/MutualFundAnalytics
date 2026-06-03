import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Check numeric return columns
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Find missing values in returns
print("Missing Return Values:")
print(df[return_cols].isnull().sum())

# Flag expense ratio anomalies
anomalies = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies:")
print(anomalies[["scheme_name", "expense_ratio_pct"]])

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned data
df.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)

print("\nScheme performance cleaned successfully")