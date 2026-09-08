# Speed Comparison between Python List and NumPy Array

import numpy as np
import time

# Create a Python list
python_list = list(range(1000000))

# Create a NumPy array
numpy_array = np.arange(1000000)

# Python list operation
start = time.time()
python_result = [x * 2 for x in python_list]
end = time.time()
print("Python list time:", end - start, "seconds")

# NumPy array operation
start = time.time()

numpy_result = numpy_array * 2

end = time.time()

print("NumPy array time:", end - start, "seconds")