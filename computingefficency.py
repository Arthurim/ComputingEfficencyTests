# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 11:52:26 2017

@author: Arthur
"""

from matplotlib import pyplot as plt
import timeit
from functools import partial

def plotF(fn, start, end, step, nTests):
    """
    Plot time complexity for a single function fn
    """
    x = []
    y = []
    for i in range(start, end, step):
        N = i
        testNTimer = timeit.Timer(partial(fn, N))
        t = testNTimer.timeit(number=nTests)
        x.append(i)
        y.append(t)
    p1 = plt.plot(x, y, 'o')
    plt.legend([p1,], [fn.__name__, ])
    plt.grid(axis='y')
    
def plotF1F(fn1, fn2, start, end, step, nTests, path, name):
    """
    Plot time complexity for a functions fn1 and fn2
    """
    x = []
    y1 = []
    y2 = []
    for i in range(start, end, step):
        N = i
        testNTimer1 = timeit.Timer(partial(fn1, N))
        t1 = testNTimer1.timeit(number=nTests)
        testNTimer2 = timeit.Timer(partial(fn1, N))
        t2 = testNTimer2.timeit(number=nTests)
        x.append(i)
        y1.append(t1)
        y2.append(t2)
    plt.plot(x, y1, 'r', label=fn1.__name__)
    plt.plot(x, y2, 'b', label=fn2.__name__)
    plt.legend(loc='upper left')
    plt.grid(axis='y') 
    plt.show()
    plt.savefig(path+name)