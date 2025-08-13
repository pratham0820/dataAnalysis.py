# Task 5: Data Analysis on CSV Files

# -----------------------------
# 1. Import Libraries
# -----------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Enable better chart visuals
sns.set_style("whitegrid")

# -----------------------------
# 2. Load the CSV File
# -----------------------------
df = pd.read_csv("sales_data.csv")

# -----------------------------
# 3. Explore the Data
# -----------------------------
print("First 5 rows:\n", df.head())
print("\nSummary Statistics:\n", df.describe())
print("\nData Info:")
print(df.info())

# -----------------------------
# 4. Basic Analysis
# -----------------------------
# Total sales
total_sales = df['Sales'].sum()
print(f"\nTotal Sales: {total_sales}")

# Sales by region
sales_by_region = df.groupby('Region')['Sales'].sum()
print("\nSales by Region:\n", sales_by_region)

# Top-selling product
top_product = df.groupby('Product')['Sales'].sum().idxmax()
print(f"\nTop Selling Product: {top_product}")

# -----------------------------
# 5. Visualizations
# -----------------------------

# Sales by Region (Bar Chart)
plt.figure(figsize=(8,5))
sns.barplot(x=sales_by_region.index, y=sales_by_region.values, palette="viridis")
plt.title("Sales by Region")
plt.ylabel("Total Sales")
plt.xlabel("Region")
plt.show()

# Sales Trend Over Time
df['Date'] = pd.to_datetime(df['Date'])
daily_sales = df.groupby('Date')['Sales'].sum()

plt.figure(figsize=(10,5))
sns.lineplot(x=daily_sales.index, y=daily_sales.values, marker="o")
plt.title("Daily Sales Trend")
plt.ylabel("Sales")
plt.xlabel("Date")
plt.show()

# Sales by Product (Pie Chart)
sales_by_product = df.groupby('Product')['Sales'].sum()
plt.figure(figsize=(6,6))
plt.pie(sales_by_product, labels=sales_by_product.index, autopct="%1.1f%%", startangle=90, colors=sns.color_palette("pastel"))
plt.title("Sales Distribution by Product")
plt.show()
