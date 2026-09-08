import pandas as pd

data = {
    "Name": ["Amit", "Riya", "Rahul", "Sneha", "Karan"],
    "Marks": [85, 72, 91, 65, 78],
    "Age": [20, 21, 20, 22, 21]
}

df = pd.DataFrame(data)

for column_name, column_data in df.items():
    print("Column:", column_name)
    print(column_data)
    print()