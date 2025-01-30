import pandas as pd
import sqlite3

def save_to_sqlite(data_file, db_name="supply_chain.db"):
    """Save the dataset into an SQLite database."""
    try:
        # Load the cleaned dataset
        data = pd.read_csv(data_file)
        print(f"Loaded data from {data_file}.")

        # Connect to SQLite database (creates file if it doesn't exist)
        conn = sqlite3.connect(db_name)
        print(f"Connected to SQLite database: {db_name}")

        # Save the DataFrame to SQLite
        table_name = "supply_chain"
        data.to_sql(table_name, conn, if_exists="replace", index=False)
        print(f"Data successfully saved to the '{table_name}' table in {db_name}.")

        # Close the connection
        conn.close()
        print("Connection closed.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    save_to_sqlite("cleaned_supply_chain_data.csv")
