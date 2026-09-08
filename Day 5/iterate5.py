import pandas as pd

data = {
    "Name": ["Amit", "Riya", "Rahul", "Sneha", "Karan"],
    "Marks": [85, 72, 91, 65, 78]
}
df = pd.DataFrame(data)

for index, row in df.iterrows():

    if row["Marks"] >= 90:
        grade = "A+"
    elif row["Marks"] >= 80:
        grade = "A"
    elif row["Marks"] >= 70:
        grade = "B"
    else:
        grade = "C"

    print(row["Name"], ":", row["Marks"], "→", grade)