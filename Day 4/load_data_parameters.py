import pandas as pd

# Load only selected columns
df = pd.read_csv(
    "D:\\Lords\\Data Science Lab\\Day 2\\Day2.2\\students3.csv",
    usecols=["ID", "Maths"],
    dtype={"ID": float, "Maths": float},
    nrows=2
)

print(df)
print(df.dtypes)