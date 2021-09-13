# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 15:02:12 2021

@author: zhou jian
"""

import numpy

l = numpy.array([1,2,3,4])
print(l)
s = l[:,numpy.newaxis]
print(s)
n = l[numpy.newaxis,:]
print(n)