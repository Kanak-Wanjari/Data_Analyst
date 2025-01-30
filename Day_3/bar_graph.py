import matplotlib.pyplot as plt

fruits = ["apple", "banana", "orange", "grapes", "mango"]
quantity = [10, 20, 15, 25, 30]

plt.bar(fruits, quantity)
plt.title("Fruits vs Quantity")
plt.xlabel("Fruits")
plt.ylabel("Quantity")
plt.show()