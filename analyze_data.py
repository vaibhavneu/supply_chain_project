import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(file_path):
    """Load the cleaned dataset."""
    try:
        data = pd.read_csv(file_path)
        print("Dataset loaded successfully.\n")
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        exit()
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        exit()


def show_dataset_overview(data):
    """Display dataset info and summary statistics."""
    print("Dataset Info:")
    print(data.info())

    print("\nSummary Statistics:")
    print(data.describe())


def analyze_top_products(data):
    """Analyze and visualize top 10 products by sales."""
    print("\nTop 10 Products by Sales:")
    top_products = (
        data.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
    print(top_products)

    # Visualization
    top_products.plot(kind="bar", title="Top 10 Products by Sales", figsize=(10, 5))
    plt.ylabel("Total Sales")
    plt.show()


def analyze_shipping_time(data):
    """Analyze and visualize average shipping time by region."""
    print("\nAverage Shipping Time by Region:")
    avg_shipping_region = data.groupby("Order Region")[
        "Days for shipping (real)"
    ].mean()
    print(avg_shipping_region)

    # Visualization
    avg_shipping_region.plot(
        kind="bar", title="Average Shipping Time by Region", figsize=(10, 5)
    )
    plt.ylabel("Average Shipping Time (Days)")
    plt.show()


def analyze_late_delivery_risk(data):
    """Analyze and visualize products with the highest late delivery risk."""
    print("\nProducts with Highest Late Delivery Risk:")
    late_risk = (
        data.groupby("Product Name")["Late_delivery_risk"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )
    print(late_risk)

    # Visualization
    late_risk.plot(
        kind="bar", title="Products with Highest Late Delivery Risk", figsize=(10, 5)
    )
    plt.ylabel("Average Late Delivery Risk")
    plt.show()


def analyze_customer_segments(data):
    """Analyze and visualize revenue by customer segments."""
    print("\nCustomer Segments by Revenue:")
    customer_segments = (
        data.groupby("Customer Segment")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )
    print(customer_segments)

    # Visualization
    customer_segments.plot(
        kind="bar", title="Revenue by Customer Segments", figsize=(10, 5)
    )
    plt.ylabel("Total Revenue")
    plt.show()


def analyze_correlation(data):
    """Analyze correlation between key metrics."""
    print("\nCorrelation Matrix:")
    correlation_matrix = data[
        ["Sales", "Late_delivery_risk", "Days for shipping (real)"]
    ].corr()
    print(correlation_matrix)

    # Heatmap visualization
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    plt.show()


def analyze_monthly_sales(data):
    """Analyze and visualize monthly sales trends."""
    # Convert order date to datetime
    data["order date (DateOrders)"] = pd.to_datetime(data["order date (DateOrders)"])
    data["OrderMonth"] = data["order date (DateOrders)"].dt.to_period("M")

    # Group by month and calculate sales
    monthly_sales = data.groupby("OrderMonth")["Sales"].sum()
    print("\nMonthly Sales Trend:")
    print(monthly_sales)

    # Visualization
    monthly_sales.plot(kind="line", title="Monthly Sales Trend", figsize=(10, 5))
    plt.ylabel("Total Sales")
    plt.xlabel("Month")
    plt.show()


def main():
    """Main function to run all analyses."""
    # Load the cleaned dataset
    file_path = "cleaned_supply_chain_data.csv"
    data = load_data(file_path)

    # Show dataset overview
    show_dataset_overview(data)

    # Perform analyses
    analyze_top_products(data)
    analyze_shipping_time(data)
    analyze_late_delivery_risk(data)
    analyze_customer_segments(data)
    analyze_correlation(data)
    analyze_monthly_sales(data)


if __name__ == "__main__":
    main()
