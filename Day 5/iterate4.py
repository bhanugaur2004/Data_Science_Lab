import pandas as pd

data = {
    "Name": ["Amit", "Riya", "Rahul", "Sneha", "Karan"],
    "Marks": [85, 72, 91, 65, 78]
}

df = pd.DataFrame(data)

for index, row in df.iterrows():
    if row["Marks"] < 70:
        df.loc[index, "Marks"] = row["Marks"] + 5

print(df)