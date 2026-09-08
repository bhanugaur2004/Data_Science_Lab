import pandas as pd

student_data = {
    "Student_ID": [101, 102, 103, 104],
    "Name": ["Rahul", "Priya", "Amit", "Neha"],
    "Age": [20, 21, 19, 20],
    "Marks": [85, 92, 78, 88]
}
# Convert dictionary into DataFrame
df = pd.DataFrame(student_data)
print("Student Data:")
print(df)
print("\nData Types:")
print(df.dtypes)
print("\nFirst 3 Students:")
print(df.head(3))
print("\nStatistical Summary:")
print(df.describe())