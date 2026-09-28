import pandas as pd

# Read cleaned data
data = pd.read_excel("Cleaned_Sales_Data.xlsx")

# Create summary values
total_revenue = data["Revenue"].sum()
total_quantity = data["Quantity"].sum()

# Revenue by product
product_summary = data.groupby("Product")["Revenue"].sum().reset_index()

# Revenue by region
region_summary = data.groupby("Region")["Revenue"].sum().reset_index()

# Create report
with pd.ExcelWriter("Automated_Report.xlsx", engine="openpyxl") as writer:

    # Main summary
    summary = pd.DataFrame({
        "Metric": ["Total Revenue", "Total Quantity", "Total Records"],
        "Value": [total_revenue, total_quantity, len(data)]
    })

    summary.to_excel(writer, sheet_name="Summary", index=False)

    # Product report
    product_summary.to_excel(
        writer,
        sheet_name="Revenue by Product",
        index=False
    )

    # Region report
    region_summary.to_excel(
        writer,
        sheet_name="Revenue by Region",
        index=False
    )

print("Automated report created successfully!")
print("Total Revenue:", total_revenue)
print("Total Quantity:", total_quantity)
print("Total Records:", len(data))