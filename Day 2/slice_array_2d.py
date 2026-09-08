import numpy as np
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(arr)
print(arr[1,1])
print(arr[2,2])
print(arr[0,0])
print("First row: ", arr[0])
print("Second row: ", arr[1])
print("Third row: ", arr[2])
print("First two rows: \n", arr[0:2])
print("First column: ", arr[:,0])
print("Second column: ", arr[:,1])
print("Third column: ", arr[:,2])
sub_array = arr[0:2, 1:3] #Rows 0 and 1, Columns 1 and 2
print("Sub-array: \n", sub_array)
