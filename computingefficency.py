# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 11:52:26 2017

@author: Arthur
"""

from matplotlib import pyplot as plt
import numpy as np
import timeit
from functools import partial
import random

def fconst(N):
    """
    O(1) function
    """
    x = 1

def flinear(N):
    """
    O(n) function
    """
    x = [i for i in range(N)]

def fsquare(N):
    """
    O(n^2) function
    """
    for i in range(N):
        for j in range(N):
            x = i*j

def fshuffle(N):
    # O(N)
    random.shuffle(list(range(N)))

def fsort(N):
    x = list(range(N))
    random.shuffle(x)
    x.sort()

def plotTC(fn, nMin, nMax, nInc, nTests):
    """
    Run timer and plot time complexity
    """
    x = []
    y = []
    for i in range(nMin, nMax, nInc):
        N = i
        testNTimer = timeit.Timer(partial(fn, N))
        t = testNTimer.timeit(number=nTests)
        x.append(i)
        y.append(t)
    p1 = plt.plot(x, y, 'o')
    plt.legend([p1,], [fn.__name__, ])
    
def plotF1F(fn1, fn2, nMin, nMax, nInc, nTests):
    """
    Run timer and plot time complexity
    """
    x = []
    y1 = []
    y2 = []
    for i in range(nMin, nMax, nInc):
        N = i
        testNTimer1 = timeit.Timer(partial(fn1, N))
        t1 = testNTimer1.timeit(number=nTests)
        testNTimer2 = timeit.Timer(partial(fn1, N))
        t2 = testNTimer2.timeit(number=nTests)
        x.append(i)
        y1.append(t1)
        y2.append(t2)
    plt.plot(x, y1, 'r')
    plt.plot(x, y2, 'b')
    plt.show()
#%%
# main() function
def main():
    print('Analyzing Algorithms...')

    plotTC(fconst, 10, 1000, 10, 10)
    plotTC(flinear, 10, 1000, 10, 10)
    plotTC(fsquare, 10, 1000, 10, 10)
    #plotTC(fshuffle, 10, 1000, 1000, 10)
    plotTC(fsort, 10, 1000, 10, 10)

    # enable this in case you want to set y axis limits
    #pyplot.ylim((-0.1, 0.5))
    
    # show plot
    pyplot.show()

# call main
if __name__ == '__main__':
    main()