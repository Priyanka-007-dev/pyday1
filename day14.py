import matplotlib.pyplot as plt

# Dataset
categories = ["FOOD", "TRAVEL", "SHOPPING"]
expenses = [500, 300, 200]

# Highlight highest category
max_index = expenses.index(max(expenses))
explode = [0.1 if i == max_index else 0 for i in range(len(expenses))]

# Create pie chart
plt.figure(figsize=(6,6))
plt.pie(
    expenses,
    labels=categories,
    autopct='%1.1f%%',   # show percentage
    explode=explode,
    shadow=True,
    startangle=90
)

# Title
plt.title("Expense Distribution")

# Equal aspect ratio ensures pie is circular
plt.axis('equal')

# Show chart
plt.show()
