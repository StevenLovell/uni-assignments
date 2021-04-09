import time
import numpy as np
import matplotlib.pyplot as plt

def mergeSort(array):
    if len(array) > 1:
        # Finds the middle of the array and then splits the array into two halves, a left half and a right half
        middle = len(array) // 2
        Left = array[:middle]
        Right = array[middle:]
        mergeSort(Left)     # Sorts the left half and then the right half
        mergeSort(Right)
        i = j = k = 0
        # Copies data to the left and right arrays depending on size
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                array[k] = Left[i]
                i += 1
            else:
                array[k] = Right[j]
                j += 1
            k += 1

        # Checks for any missed numbers
        while i < len(Left):
            array[k] = Left[i]
            i += 1
            k += 1
        while j < len(Right):
            array[k] = Right[j]
            j += 1
            k += 1

dict1 = {}  # Using a dictionary to store the time taken to sort each step.
for i in range(1, 10):  # This creates 9 lists from 100,000 to 900,000 and measures the time taken to sort the lists.
    array = np.random.randint(0, i * 5000, i * 100000) # Creates a list of numbers from 0-5000.
    start = time.process_time()     #Used to measure the process time of each sort.
    mergeSort(array)                 # Runs the sorting algorithm within the for loop.
    end = time.process_time()
    dict1[len(array)] = (end - start)   # Saves the data to a dictionary.
    print("Time for " + str(len(array)) + " numbers is " + str(dict1[len(array)]))
plt.xlabel("Numbers in array")      # Creates a line diagram from the data.
plt.ylabel("Time")
plt.title("Merge Sort Time")
plt.plot(*zip(*sorted(dict1.items())))
plt.show()
