import matplotlib.pyplot as plt

# Dataset
dates = ["MON", "TUE", "WED", "THU", "FRI"]
sales = [200, 250, 300, 280, 350]

# Find highest and lowest
max_sales = max(sales)
min_sales = min(sales)

max_index = sales.index(max_sales)
min_index = sales.index(min_sales)

# Plot line chart
plt.plot(dates, sales, marker='o', linestyle='-')

# Highlight highest and lowest points
plt.scatter(dates[max_index], max_sales)
plt.scatter(dates[min_index], min_sales)

# Add labels for points
plt.text(dates[max_index], max_sales, f"High: {max_sales}")
plt.text(dates[min_index], min_sales, f"Low: {min_sales}")

# Labels and title
plt.xlabel("Days")
plt.ylabel("Sales")
plt.title("Sales Trend Visualization")

# Show grid
plt.grid()

# Show plot
plt.show()
