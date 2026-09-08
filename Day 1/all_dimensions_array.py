#   Array of all dimensions in NumPy

import numpy as np

# 1D array
arr1 = np.array([10, 20, 30, 40])

# 2D array
arr2 = np.array([
    [10, 20],
    [30, 40]
])

# 3D array
arr3 = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print("1D Array:")
print(arr1)

print("\n2D Array:")
print(arr2)

print("\n3D Array:")
print(arr3)

print("Dimensions of arr1:", arr1.ndim)
print("Dimensions of arr2:", arr2.ndim)
print("Dimensions of arr3:", arr3.ndim)