# Read CSV file
data = []

with open("sales.csv", "r") as file:
    lines = file.readlines()

# Extract headers
headers = lines[0].strip().split(",")

# Process data
for line in lines[1:]:
    values = line.strip().split(",")
    
    record = {
        "PRODUCT": values[0],
        "QUANTITY": int(values[1]),
        "PRICE": int(values[2])
    }
    
    # Bonus: add TOTAL column
    record["TOTAL"] = record["QUANTITY"] * record["PRICE"]
    
    data.append(record)

# 🔹 Calculate total sales per product
sales_per_product = {}

for record in data:
    product = record["PRODUCT"]
    total = record["TOTAL"]
    
    if product in sales_per_product:
        sales_per_product[product] += total
    else:
        sales_per_product[product] = total

# 🔹 Total revenue
total_revenue = sum(sales_per_product.values())

# 🔹 Top-selling product
top_product = max(sales_per_product, key=sales_per_product.get)

# 🔹 Sort by revenue (bonus)
sorted_sales = sorted(sales_per_product.items(), key=lambda x: x[1], reverse=True)

# 🔹 Output
print("Sales per Product:")
for product, total in sales_per_product.items():
    print(f"{product}: {total}")

print("\nTotal Revenue:", total_revenue)
print("Top-Selling Product:", top_product)

print("\nSorted by Revenue:")
for product, total in sorted_sales:
    print(f"{product}: {total}")
