import pandas as pd

df = pd.read_csv("D:\\Lords\\Data Science Lab\\Day 2\\Day2.2\\students3.csv")

# Rename columns
df.rename(columns={
    "ID": "Student_Name",
    "Maths": "Student_Age",
    "Science": "Program"
}, inplace=True)

print(df)