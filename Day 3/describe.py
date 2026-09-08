import pandas as pd

df = pd.read_csv("D:\\Lords\\Data Science Lab\\Day 2\\Day2.2\\students.csv")

# Display statistical summary
print(df.describe())
# print(df.describe(include="all"))