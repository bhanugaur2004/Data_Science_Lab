# Memory Comparison between Python List and NumPy Array

import numpy as np
import sys

# Create a Python list
python_list = list(range(1000))

# Create a NumPy array
numpy_array = np.arange(1000)

print("Memory used by Python list:",
      sys.getsizeof(python_list))

print("Memory used by NumPy array:",
      numpy_array.nbytes)