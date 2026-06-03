import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

nav_data = data["data"]

df = pd.DataFrame(nav_data)

print(df.head())

df.to_csv(
    "data/raw/hdfc_top100_live_nav.csv",
    index=False
)

print("Live NAV data saved successfully")