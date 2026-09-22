import matplotlib.pyplot as plt

companies = ["Company A", "Company B", "Company C", "Company D"]
market_share = [35, 30, 20, 15]

plt.pie(market_share, labels=companies)

plt.title("Market Share")
plt.show()