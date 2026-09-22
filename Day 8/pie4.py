import matplotlib.pyplot as plt

companies = ["Company A", "Company B", "Company C", "Company D"]
market_share = [35, 30, 20, 15]

colors = ["red", "blue", "green", "orange"]

explode = [0.1, 0, 0, 0]

plt.pie(
    market_share,
    labels=companies,
    autopct="%1.1f%%",
    explode=explode,
    colors=colors,
    shadow=True
)

plt.title("Market Share")
plt.show()