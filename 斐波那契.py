# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 07:25:57 2020

@author: zhou jian
"""


import time 

def time_cost(f):
    def _f(*arg, **kwarg):
        start = time.clock()
        a = f(*arg, **kwarg)
        end = time.clock()
        print (f.__name__,"run cost time is",end-start)
        return a
    return _f

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
@time_cost
def fib_opt(n):
    a, b, i =0,1,1
    
    while i <n:
        a,b = b,a+b
        i +=1
    else:
        return b
    
N =35
print (time_cost(fib)(N))
print (fib_opt(N))
