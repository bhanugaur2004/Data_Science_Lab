import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

result = arr[[0, 2, 4]]
result2 = arr[[5, 1, 3]]

print("Original array:", arr)
print("Selected elements:", result)
print("Selected elements:", result2)