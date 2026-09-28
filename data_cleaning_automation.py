import pandas as pd

# 1. Read the raw Excel file
data = pd.read_excel("Raw_Sales_Data.xlsx")

print("Raw data loaded successfully!")
print("Rows before cleaning:", len(data))

# 2. Remove duplicate rows
data = data.drop_duplicates()

# 3. Remove extra spaces from text columns
data["Product"] = data["Product"].str.strip()
data["Region"] = data["Region"].str.strip()

# 4. Fix inconsistent product names
data["Product"] = data["Product"].replace({
    "laptop": "Laptop",
    "LAPTOP": "Laptop",
    "Smart Phone": "Smartphone",
    "smartphone": "Smartphone",
    "tablet": "Tablet",
    "TABLET": "Tablet",
    "headphones": "Headphones",
    "Head phone": "Headphones",
    "keyboard": "Keyboard",
    "KEYBOARD": "Keyboard",
    "mouse": "Mouse",
    "MOUSE": "Mouse",
    "monitor": "Monitor",
    "MONITOR": "Monitor",
    "printer": "Printer",
    "PRINTER": "Printer",
    "office chair": "Office Chair",
    "Office chair": "Office Chair",
    "desk": "Desk",
    "DESK": "Desk"
})

# 5. Fix inconsistent region names
data["Region"] = data["Region"].replace({
    "north": "North",
    "NORTH": "North",
    "south": "South",
    "SOUTH": "South",
    "east": "East",
    "EAST": "East",
    "west": "West",
    "WEST": "West"
})

# 6. Fill missing values
data["Product"] = data["Product"].fillna("Unknown")
data["Region"] = data["Region"].fillna("Unknown")
data["Quantity"] = data["Quantity"].fillna(data["Quantity"].median())

# 7. Calculate Revenue
data["Revenue"] = data["Quantity"] * data["Unit Price"]

# 8. Save cleaned data
data.to_excel("Cleaned_Sales_Data.xlsx", index=False)

print("Rows after cleaning:", len(data))
print("Missing values handled!")
print("Duplicates removed!")
print("Inconsistent data fixed!")
print("Cleaned_Sales_Data.xlsx created successfully!")