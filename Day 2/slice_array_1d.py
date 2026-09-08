import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70])

print("Original array:", arr)

print("Elements from index 1 to 4:", arr[1:5])
print("First 3 elements:", arr[:3])
print("Last 3 elements:", arr[-3:])
print("Every second element:", arr[::2])