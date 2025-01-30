import matplotlib.pyplot as plt

# Data
fruits = ["apple", "banana", "orange", "grapes", "mango"]
quantity = [10, 20, 15, 25, 30]
colors = ['red', 'yellow', 'orange', 'purple', 'green']
hatch_patterns = ['/', '\\', '|', '-', '+']

# Create Bar Graph with customizations
plt.figure(figsize=(8, 5))  # Adjust figure size
bars = plt.bar(fruits, quantity, color=colors, edgecolor='black', width=0.6)

# Adding values on top of bars
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             str(bar.get_height()), ha='center', fontsize=12, fontweight='bold')

# Applying hatch patterns to bars
for bar, pattern in zip(bars, hatch_patterns):
    bar.set_hatch(pattern)

# Labels and Title
plt.title("Fruits vs Quantity", fontsize=14, fontweight='bold')
plt.xlabel("Fruits", fontsize=12)
plt.ylabel("Quantity", fontsize=12)

# Rotating x-axis labels
plt.xticks(rotation=15)

# Adding grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the graph
plt.show()