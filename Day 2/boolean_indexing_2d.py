import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

result = arr[arr > 50]

print("Elements greater than 50:")
print(result)