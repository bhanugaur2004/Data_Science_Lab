import numpy as np

data = np.loadtxt("D:\\Lords\\Data Science Lab\\Day 2\\Day2.2\\students.csv", delimiter=",")

print("Data:")
print(data)

print("Shape:", data.shape)
print("Number of rows:", data.shape[0])
print("Number of columns:", data.shape[1])
