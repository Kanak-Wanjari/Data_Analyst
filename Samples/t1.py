import matplotlib.pyplot as plt

heights = [150, 160, 170, 180, 190]
weights = [50, 60, 70, 80, 90]

plt.scatter(heights, weights, color='green')
plt.title('Height vs Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()