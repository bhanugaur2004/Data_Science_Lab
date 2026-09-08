import pandas as pd
import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")

# Create sample data
data = {
    "id": [1, 2, 3],
    "name": ["Amit", "Rahul", "Priya"],
    "marks": [85, 90, 78]
}

df = pd.DataFrame(data)

# Store data in SQL table
df.to_sql("students", conn, if_exists="replace", index=False)

# Load data using read_sql()
result = pd.read_sql("SELECT * FROM students", conn)

print(result)

conn.close()