from functools import lru_cache  # Imports the cache function from the functools module


def fibonacci_recursive(Number):  # Creates the fibonacci function
    # The below print statement shows how many times fibonacci_recursive runs.
   # print("Calculating Fibonacci ", "(", Number, ")", sep="", end=",\n ")
    # The first 2 fibonacci numbers are 0 and 1, the program loops backwards without the if and elif statements
    if Number == 0:
        return 0
    elif Number == 1:
        return 1
    else:
        return fibonacci_recursive(Number - 1) + fibonacci_recursive(Number - 2)


@lru_cache(maxsize=None)  # Loads the cache decorator.
def fibonacci_cache(Number):
   # print("Calculating Fibonacci ", "(", Number, ")", sep="", end=",\n ")
    if Number == 0:
        return 0
    elif Number == 1:
        return 1
    else:
        return fibonacci_cache(Number - 1) + fibonacci_cache(Number - 2)


def fibonacci_iterative(Number):  # For loops are iterative functions rather than recursive
    #print("Calculating Fibonacci ", "(", Number, ")", sep="", end=",\n ")
    old, new = 0, 1
    if Number == 0:
        return 0
    for i in range(Number - 1):
        old, new = new, old + new
    return new


# Saves the output of fibonacci_recursive to output.txt. Used to measure recursion.
from contextlib import redirect_stdout

with open('output.txt', 'w') as f:
    with redirect_stdout(f):
        print(fibonacci_recursive(10))
