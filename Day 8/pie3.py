import matplotlib.pyplot as plt

companies = ["Company A", "Company B", "Company C", "Company D"]
market_share = [35, 30, 20, 15]

explode = [0.1, 0, 0, 0]

plt.pie(
    market_share,
    labels=companies,
    autopct="%1.1f%%",
    explode=explode
)

plt.title("Market Share")
plt.show()