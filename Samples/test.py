import matplotlib.pyplot as plt

# Data
categories = ['Apples', 'Bananas', 'Cherries']
sales = [50, 70, 30]

# Create bar plot
plt.bar(categories, sales, color='skyblue')
plt.title('Fruit Sales')
plt.xlabel('Fruits')
plt.ylabel('Number Sold')
plt.show()


import matplotlib.pyplot as plt

# Data
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
temperatures = [30, 32, 31, 29, 35]

# Create line plot
plt.plot(days, temperatures, marker='o', color='blue')
plt.title('Daily Temperatures')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.show()


import matplotlib.pyplot as plt

# Data
heights = [150, 160, 170, 180, 190]
weights = [50, 60, 70, 80, 90]

# Create scatter plot
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
plt.pie(expenses, labels=categories, autopct='%1.1f%%', startangle=90)
plt.title('Monthly Expenses')
plt.show()


import matplotlib.pyplot as plt

# Data
categories = ['Python', 'Java', 'C++']
popularity = [85, 75, 65]

# Create horizontal bar plot
plt.barh(categories, popularity, color='orange')
plt.title('Programming Language Popularity')
plt.xlabel('Popularity (%)')
plt.ylabel('Languages')
plt.show()