# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 11:34:28 2017

@author: Arthur
"""
from scipy.constants import golden
import numpy as np
import timeit

def Fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibo(n-1) + Fibo(n-2)
    
def Binet(n):
    return int(round((1/np.sqrt(5))*(golden**n +(1-golden)**n)))
    #%%