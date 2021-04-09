# Imports the the timer function from the timeit module which is used to measure the execution time.
from timeit import Timer

# Loops through each fibonacci iteration and prints out the fibonacci number and time taken in seconds.
for i in range(1,10):
    fr='fibonacci_recursive('+str(i)+')'
    timer1 = Timer(fr, 'from fibonacci_comparison import fibonacci_recursive')
    time1 = timer1.timeit(3)

    fc = 'fibonacci_cache('+str(i)+')'
    timer2 = Timer(fc, 'from fibonacci_comparison import fibonacci_cache')
    time2 = timer2.timeit(3)

    fi = 'fibonacci_iterative('+str(i)+')'
    timer3 = Timer(fi, 'from fibonacci_comparison import fibonacci_iterative')
    time3 = timer3.timeit(3)

    print(f'Fibonacci number={i:2d}, fibonacci_recursive: {time1:f} seconds, fibonacci_cache: {time2:f} seconds, fibonbacci_iterative: {time3:f} seconds')
