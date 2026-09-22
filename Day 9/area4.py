import matplotlib.pyplot as plt

time = ["10 AM", "11 AM", "12 PM", "1 PM", "2 PM", "3 PM", "4 PM"]
cpu_usage = [30, 45, 60, 75, 55, 80, 65]

plt.plot(time, cpu_usage, marker="o")
plt.fill_between(time, cpu_usage, alpha=0.4)

plt.title("CPU Usage Over Time")
plt.xlabel("Time")
plt.ylabel("CPU Usage (%)")

plt.ylim(0, 100)
plt.grid(True)

plt.show()