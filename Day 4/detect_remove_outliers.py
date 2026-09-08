import pandas as pd

data = {
    "Marks": [45, 50, 55, 60, 65, 70, 75, 200]
}

df = pd.DataFrame(data)

# Calculate Quartiles
Q1 = df["Marks"].quantile(0.25)
Q3 = df["Marks"].quantile(0.75)

print("Q1:", Q1)
print("Q3:", Q3)

# Calculate IQR  - Interquartile Range
IQR = Q3 - Q1 

print("IQR:", IQR)

# Calculate limits
lower_limit = Q1 - 1.5 * IQR #This is lower limit for outliers, below this limit, the data is considered as outlier
upper_limit = Q3 + 1.5 * IQR #This is upper limit for outliers, above this limit, the data is considered as outlier

print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

# Remove outliers
clean_df = df[
    (df["Marks"] >= lower_limit) &
    (df["Marks"] <= upper_limit)
]

print("Original Data:")
print(df)

print("\nData After Removing Outliers:")
print(clean_df)