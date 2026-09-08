# Reshaping an Array in NumPy

import numpy as np

# Create an array from 0 to 20
arr = np.arange(21)

print("Original array:")
print(arr)

# Reshape the array
new_arr = arr.reshape(3, 7)

print("\nReshaped array:")
print(new_arr)