import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import skew

# Sample dataset (you can change values)
data = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 60, 70, 80, 90]

# Create histogram with KDE curve
plt.figure(figsize=(8, 5))
sns.histplot(data, kde=True)

# Labels and title
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

# Show plot
plt.show()

# Calculate skewness
skew_value = skew(data)

print("Skewness value:", skew_value)

# Identify skewness type
if skew_value > 0:
    print("Data is Positively Skewed (Right Skewed)")
elif skew_value < 0:
    print("Data is Negatively Skewed (Left Skewed)")
else:
    print("Data is Symmetrical")
