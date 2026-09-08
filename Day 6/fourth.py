import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May"]

product_a = [100, 150, 130, 180, 220]
product_b = [80, 120, 160, 170, 200]

plt.plot(
    months,
    product_a,
    marker="o",
    label="Product A"
)

plt.plot(
    months,
    product_b,
    marker="s",
    label="Product B"
)

plt.title("Product Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid()
plt.legend()

plt.savefig("product_sales_comparison.png")  # Save the plot as a PNG file

plt.show()