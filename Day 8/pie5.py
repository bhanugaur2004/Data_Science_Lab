import matplotlib.pyplot as plt

companies = ["Company A", "Company B", "Company C", "Company D"]
market_share = [35, 30, 20, 15]

plt.pie(
    market_share,
    labels=companies,
    autopct="%1.1f%%",
    wedgeprops={"width": 0.4}
)

plt.title("Market Share - Donut Chart")
plt.show()