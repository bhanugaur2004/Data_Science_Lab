import numpy as np

# data = np.loadtxt("D:\\Lords\\Data Science Lab\\Day 2\\Day2.2\\students3.csv", delimiter=",", skiprows=1)

data = np.genfromtxt("D:\\Lords\\Data Science Lab\\Day 2\\Day2.2\\students3.csv", delimiter=",", skip_header=1)

print(data)

#nan = Not a number
print("\nMissing value positions:")
print(np.isnan(data))

data[np.isnan(data)] = 0

print(data)