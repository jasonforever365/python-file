# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 08:32:38 2020

@author: zhou jian
"""


def largerx(x):
    def echo(value):
        return True if value > x[0] else False
    return echo

def pow_y(x):
    def echo(value):
        x[0] = x[0]*2
        return value**x[0], value**x[1]
    return echo

if __name__ == "__main__":
    lst2 = pow_y([1,2])
    print ("closure powy", lst2(2))
    print ("closure powy", lst2(3))
    print ("closure powy", lst2(4))
    
    x = [10]
    larger10 = largerx(x)
    print (x[0], larger10(2))
    x[0] =1
    print (x[0], larger10(2))
    x[0] =100
    print (x, larger10(2))
    