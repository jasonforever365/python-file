# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 20:47:55 2020

@author: zhou jian
"""


def decorator(f):
    print ("before"+f.__name__ + "called.")
    return f

def myfunc1():
    print ("myfunc1() called.")
    
@decorator
def myfunc2():
    print ("myfunc2() called.")
    
if __name__ == "__main__":
    decorator(myfunc1)()
    mufunc2()
    