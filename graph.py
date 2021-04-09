import matplotlib.pyplot as plt

def smallSquare():  # Creates a small red square
    x=[3,3,4,4,3]
    y=[3,4,4,3,3]
    plt.plot(x,y,'r:o')

def mediumSquare(): # creates a medium green square
    x=[2, 2, 5, 5, 2]
    y=[2, 5, 5, 2, 2]
    plt.plot(x, y, 'g:s')

def largeSquare():  # creates a large blue square
    x=[1,1,6,6,1]
    y=[1,6,6,1,1]
    plt.plot(x,y,'b-x')

def run():
    smallSquare()
    mediumSquare()
    largeSquare()
    plt.show()
run()
