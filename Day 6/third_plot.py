import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May"]
sales = [100, 150, 130, 180, 220]

plt.plot(
    months,
    sales,
    linestyle="--",
    marker="s",
    color="red",
    linewidth=2
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid()

plt.show()