import matplotlib.pyplot as plt

companies = ["Company A", "Company B", "Company C", "Company D"]
market_share = [35, 30, 20, 16]

plt.pie(
    market_share,
    labels=companies,
    autopct="%1.1f%%"
)

plt.title("Market Share")
plt.show()
