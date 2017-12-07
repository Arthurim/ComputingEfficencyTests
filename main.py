# -*- coding: utf-8 -*-
"""
Created on Thu Dec 5 12:31:25 2017

@author: Arthur
"""
from fibofunctions import Fibo, Binet
from computingefficency import plotF1F

def main():
    path = "C:\\Users\\Arthur\\Documents\\info\\fibo\\"
    plotF1F(Fibo, Binet, 0, 1000, 1, 10, path, 'FiboBinetComparison')

if __name__ == '__main__':
    main()