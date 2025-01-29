import matplotlib.pyplot as plt

fruits = ['Apple', 'Banana', 'mango', 'orange', 'grapes']
quantity =[10 , 15, 20, 30, 5]

plt.bar(fruits, quantity, color=['red', 'yellow', 'green'])
plt.title('Fruits Quantity Graph')
plt.xlabel('Fruits')
plt.ylabel('Qunatity')
plt.show()

# Line chart for comparison
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
sales = [200, 250, 300, 280, 320]

plt.plot(days, sales, marker='o')
plt.title('Sales Over Days')
plt.xlabel('Days')
plt.ylabel('Sales')
plt.show()

# Data
scores = [55, 65, 70, 75, 80, 85, 90, 95, 100]

# Histogram
plt.hist(scores, bins=5, color='purple')
plt.title('Score Distribution')
plt.xlabel('Score Range')
plt.ylabel('Frequency')
plt.show()

# Data
heights = [150, 160, 170, 180, 190]
weights = [50, 60, 65, 75, 85]

# Scatter plot
plt.scatter(heights, weights, color='green')
plt.title('Height vs Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()

import matplotlib.pyplot as plt

# Data
expenses = [500, 300, 200]
categories = ['Rent', 'Groceries', 'Entertainment']

# Create pie chart
plt.pie(expenses, labels=categories, autopct='%1.f%%', startangle=90)
plt.title('Monthly Expenses')
plt.show()