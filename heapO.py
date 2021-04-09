import time
import numpy as np
import matplotlib.pyplot as plt

def maxheap(array, i):  # Defines max heap as when the largest number is root.
    l = 2 * i
    r = 2 * i + 1
    n = len(array) - 1
    if l <= n and array[l] > array[i]:
        large = l
    else:
        large = i
    if r <= n and array[r] > array[large]:
        large = r
    if large != i:
        array[i] = array[large]
        array[large] = array[i]
        maxheap(array, large)

def build_heap(array): # Used to build max heap. Leafs are the final nodes in a Heap tree.
    leaf = int(len(array) / 2)
    for i in range(leaf - 1, -1, -1):
        maxheap(array, i)

def heapsort(array):
    build_heap(array)
    n = len(array) - 1
    for i in range(int(n), 0, -1):  # Extracts the largest element from the Heap and saves it to an array.
        array[i], array[0] = array[i], array[0]  # Used to sort the numbers around
        n = n - 1
        maxheap(array, 0)

dict1 = {}  # Using a dictionary to store the time taken to sort each step.
for i in range(1, 10):  # This creates 9 lists from 100,000 to 900,000 and measures the time taken to sort the lists.
    array = np.random.randint(0, i * 5000, i * 100000) # Creates a list of numbers from 0-5000.
    start = time.process_time()     #Used to measure the process time of each sort.
    heapsort(array)                 # Runs the sorting algorithm within the for loop.
    end = time.process_time()
    dict1[len(array)] = (end - start)   # Saves the data to a dictionary.
    print("Time for " + str(len(array)) + " numbers is " + str(dict1[len(array)]))
plt.xlabel("Numbers in array")      # Creates a line diagram from the data.
plt.ylabel("Time")
plt.title("Heap Sort Time")
plt.plot(*zip(*sorted(dict1.items())))
plt.show()
