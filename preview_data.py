import pandas as pd

# Step 1: Load the dataset
print("Loading dataset...")
main_data = pd.read_csv("DataCoSupplyChainDataset.csv", encoding="ISO-8859-1")

# Step 2: Preview the dataset
print("\nDataset Preview:")
print(main_data.head())  # Show the first 5 rows

# Step 3: Dataset info and missing values
print("\nDataset Info:")
print(main_data.info())  # Overview of columns, data types, and non-null counts

print("\nMissing Values in Each Column:")
print(main_data.isnull().sum())  # Check missing values per column

# Step 4: Drop irrelevant or empty columns
columns_to_drop = ["Order Zipcode", "Product Description"]  # Drop columns with excessive missing values or irrelevance
cleaned_data = main_data.drop(columns=columns_to_drop)

# Step 5: Handle missing values
# Fill missing values in 'Customer Lname' with 'Unknown'
cleaned_data["Customer Lname"] = cleaned_data["Customer Lname"].fillna("Unknown")

# Fill missing values in 'Customer Zipcode' with 0
cleaned_data["Customer Zipcode"] = cleaned_data["Customer Zipcode"].fillna(0)

# Step 6: Normalize numerical columns for further analysis (optional)
# Example: Normalizing 'Days for shipping (real)'
numerical_columns = ["Days for shipping (real)", "Days for shipment (scheduled)", "Sales", "Order Item Total"]
for column in numerical_columns:
    if column in cleaned_data.columns:
        cleaned_data[column] = cleaned_data[column] / cleaned_data[column].max()

# Step 7: Save the cleaned data to a new CSV
cleaned_data.to_csv("cleaned_supply_chain_data.csv", index=False)
print("\nCleaned data saved as 'cleaned_supply_chain_data.csv'.")

# Step 8: Final preview of cleaned data
print("\nCleaned Data Preview:")
print(cleaned_data.head())
