import pandas as pd

data = {
    "Name": ["Amit", "Riya", "Rahul", "Sneha", "Karan"],
    "Marks": [85, 72, 91, 65, 78],
    "Age": [20, 21, 20, 22, 21]
}

df = pd.DataFrame(data)

for index, row in df.iterrows():
    print("Index:", index)
    print("Name:", row["Name"])
    print("Marks:", row["Marks"])
    print("Age:", row["Age"])
    print()