import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit"],
    "Marks": [85, 92, 78]
}
df = pd.DataFrame(data)
print(df)
print()
print()
print()
df.rename(index={
    0: "Student_1",
    1: "Student_2",
    2: "Student_3"
}, inplace=True)

print(df)