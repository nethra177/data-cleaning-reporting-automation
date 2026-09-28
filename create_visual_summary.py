import pandas as pd
import matplotlib.pyplot as plt

# Read cleaned data
data = pd.read_excel("Cleaned_Sales_Data.xlsx")

# Create revenue summary by product
summary = data.groupby("Product")["Revenue"].sum().sort_values()

# Create bar chart
plt.figure(figsize=(10, 6))

plt.barh(summary.index, summary.values)

plt.xlabel("Revenue")
plt.ylabel("Product")
plt.title("Revenue by Product")

plt.tight_layout()

# Save the chart
plt.savefig("Sales_Summary.png")

plt.show()

print("Sales summary chart created successfully!")