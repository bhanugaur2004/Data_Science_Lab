import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y1 = [10, 20, 15, 30, 25]
y2 = [5, 15, 20, 25, 35]

plt.fill_between(x, y1, alpha=0.3, label="Product A")
plt.fill_between(x, y2, alpha=0.3, label="Product B")

plt.plot(x, y1)
plt.plot(x, y2)

plt.xlabel("Time")
plt.ylabel("Value")
plt.title("Area Chart with Transparency")
plt.legend()

plt.show()