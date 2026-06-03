import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Convert transaction date
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Keep only positive amounts
df = df[df["amount_inr"] > 0]

# Check KYC values
print("KYC Status Values:")
print(df["kyc_status"].unique())

# Remove duplicates
df = df.drop_duplicates()

print("Shape after cleaning:", df.shape)

# Save cleaned file
df.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)

print("Investor transactions cleaned successfully")