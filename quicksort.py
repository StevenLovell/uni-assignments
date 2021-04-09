import time
import numpy as np
import matplotlib.pyplot as plt

# This function partitions the data from an array. Low is the smallest number and high is the last index.
def partition(array, low, high):
    i = (low - 1)  # Sets the index for the smallest number
    pivot = array[high]  # Takes the pivot point from the last number in an array
    # If the number is smaller or same as the pivot it is placed to the left. Higher is placed to the right
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return (i + 1)


def quickSort(array, low, high):  #
    if len(array) == 1:
        return array
    if low < high:  # Low is the first index and high is the last index.
        PartitionIndex = partition(array, low, high)
        quickSort(array, low, PartitionIndex - 1)   # If data is lower move left one
        quickSort(array, PartitionIndex + 1, high)  # If data is higher move right one


dict1 = {}  # Using a dictionary to store the time taken to sort each step.
for i in range(1, 10):  # This creates 9 lists from 100,000 to 900,000 and measures the time taken to sort the lists.
    array = np.random.randint(0, i * 5000, i * 100000)  # Creates a list of numbers from 0-5000.
    n = len(array)
    start = time.process_time()  # Used to measure the process time of each sort.
    quickSort(array, 0, n - 1)  # Runs the sorting algorithm within the for loop.
    end = time.process_time()
    dict1[len(array)] = (end - start)  # Saves the data to a dictionary.
    print("Time for " + str(len(array)) + " numbers is " + str(dict1[len(array)]))
plt.xlabel("Numbers in array")  # Creates a line diagram from the data.
plt.ylabel("Time")
plt.title("Quick Sort Time Complexity")
plt.plot(*zip(*sorted(dict1.items())))
plt.show()
