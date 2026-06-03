import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(
    ["amfi_code", "date"]
)

df = df.drop_duplicates()

df = df[df["nav"] > 0]

print(df.shape)

df.to_csv(
    "data/processed/02_nav_history_cleaned.csv",
    index=False
)

print("Cleaned NAV file saved")