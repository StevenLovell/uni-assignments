from binarytree import tree,bst,heap
# Generates a random tree, binary tree and a random heap.
randomTree = tree(height=3, is_perfect=False)
randomBst = bst(height=3, is_perfect=True)
randomHeap = heap(height=3, is_max=True, is_perfect=False)

print(randomTree)
print(randomBst)
print(randomHeap)
