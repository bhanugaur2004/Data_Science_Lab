import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [20, 35, 30, 45, 50, 65]

plt.plot(months, sales, marker="o")
plt.fill_between(months, sales, alpha=0.4)

plt.title("Monthly Sales - Area Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

plt.show()
