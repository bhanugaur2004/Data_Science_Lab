import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

result = arr[arr > 50]
# result = arr > 50

print("Original array:", arr)
print("Numbers greater than 50:", result)

result2 = arr[(arr >= 30) & (arr <= 70)]

print("Numbers between 30 and 70:", result2)