import heapq

Heap = [60,12,55,30,42,5,23,14,8,20]

def childNodes(i):  # defines the child nodes. The tree is filled from left to right.
     return (2*i)+1, (2*i)+2

def createTree(Heap, i=0, d = 0):  # creates the tree
    if i >= len(Heap):
        return
    left, right =  childNodes(i)
    createTree(Heap, right, d =d + 1)
    print("      " * d + str(Heap[i]))  # Sets the spaces between the numbers
    createTree(Heap, left, d =d + 1)

heapq.heapify(Heap)         # creates a min heap
print('A min heap', Heap)
createTree(Heap)
heapq._heapify_max(Heap)    # creates a max heap
print('A max heap', Heap)
createTree(Heap)

