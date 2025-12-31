import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

print("📊 DATASET PREVIEW")
print(df.head())

# Dataset info
print("\nℹ️ DATASET INFORMATION")
print(df.info())

# Handling missing values
df['Quantity'].fillna(0, inplace=True)
df['Total_Sales'].fillna(df['Quantity'] * df['Price'], inplace=True)

# Remove duplicate rows if any
df.drop_duplicates(inplace=True)

print("\n✅ CLEANED DATA")
print(df)

# Analysis
total_revenue = df['Total_Sales'].sum()
average_sales = df['Total_Sales'].mean()
highest_sale = df['Total_Sales'].max()
lowest_sale = df['Total_Sales'].min()

best_selling_product = df.groupby('Product')['Total_Sales'].sum().idxmax()

# Report
print("\n📈 SALES ANALYSIS REPORT")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Average Sale Value: ₹{average_sales:,.2f}")
print(f"Highest Sale: ₹{highest_sale:,.2f}")
print(f"Lowest Sale: ₹{lowest_sale:,.2f}")
print(f"Best Selling Product: {best_selling_product}")
