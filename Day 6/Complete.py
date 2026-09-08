import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May"]

product_a = [100, 150, 130, 180, 220]
product_b = [80, 120, 160, 170, 200]

# Plot Product A
plt.plot(
    months,
    product_a,
    linestyle="-",
    marker="o",
    color="blue",
    linewidth=2,
    label="Product A"
)

# Plot Product B
plt.plot(
    months,
    product_b,
    linestyle="--",
    marker="s",
    color="green",
    linewidth=2,
    label="Product B"
)

# Title
plt.title("Monthly Sales Comparison")

# Axis labels
plt.xlabel("Month")
plt.ylabel("Sales")

# Grid
plt.grid()

# Legend
plt.legend()

# Save graph
plt.savefig("sales_comparison.png")

# Display graph
plt.show()