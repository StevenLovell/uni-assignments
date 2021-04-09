import numpy as np
import sys

# creating a random list and array with a 1000 elements
List = range(1000)
Array = np.arange(1000)

# comparing the size of each element
print("Each element in a list is: ", sys.getsizeof(List),'bytes')
print("Each element in a NumPy array is: ", Array.itemsize,'bytes')
# Comparing the size of the whole list and array.
print("The size of a list with 1000 elements is: ", sys.getsizeof(List) * len(List),'bytes')
print("The size of an array with 1000 elements is: ", Array.size * Array.itemsize,'bytes')
