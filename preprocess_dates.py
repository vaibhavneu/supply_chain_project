import pandas as pd

# Load the dataset
data = pd.read_csv("cleaned_supply_chain_data.csv")

# Convert 'order date (DateOrders)' to SQLite-compatible format
data["order date (DateOrders)"] = pd.to_datetime(
    data["order date (DateOrders)"], format="%m/%d/%Y %H:%M", errors="coerce"
)

# Save the cleaned dataset
data.to_csv("cleaned_supply_chain_data_fixed.csv", index=False)

print("Dates have been processed and saved to 'cleaned_supply_chain_data_fixed.csv'.")
