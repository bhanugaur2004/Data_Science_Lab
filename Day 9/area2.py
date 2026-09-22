import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

google = [40, 50, 55, 60, 70, 80]
youtube = [20, 25, 30, 35, 40, 45]
facebook = [15, 20, 18, 25, 30, 35]

plt.stackplot(
    months,
    google,
    youtube,
    facebook,
    labels=["Google", "YouTube", "Facebook"],
    alpha=0.7
)

plt.title("Website Traffic Sources")
plt.xlabel("Month")
plt.ylabel("Visitors")
plt.legend(loc="upper left")

plt.show()