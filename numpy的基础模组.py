# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:17:27 2021

@author: zhou jian
"""


import numpy as np
from numpy import pi
print(np.arange(15))
a = np.arange(15).reshape(3,5)
print(a)

print(a.shape)

print(a.ndim)
#ndim是axes/dimensions的数量

print(a.dtype.name)
print(a.size)
print(np.zeros((3,4)))

#print (np.linspace(0, 2*pi, 100))

c = np.array([[2,1],[0,1]])
b = np.array([[2,3],[4,5]])
print(b*c)
print(b.dot(c))
print(np.dot(b,c))

d = np.arange(3)
print(np.exp(d)) #exp表示e
print(np.sqrt(d)) #sqrd表示开更号

e = np.floor(10*np.random.random((3,4)))
#np.floor向下取整
print(e)
print(e.ravel())
#ravel讲多维数据变成一维的

f = np.floor(10*np.random.random((2,2)))
g = np.floor(10*np.random.random((2,2)))
print(f)
print(g)
print(np.hstack((f,g)))
print(np.vstack((f,g)))
#hstack是横着拼接

h = np.floor(10*np.random.random((2,12)))
print(h)
print(np.hsplit(h,3))
#3是指按照3个array来切分
print(np.hsplit(h,(3,4)))
#(3,4)是指的按照3列和4列切分
print(np.vsplit(h,2))

i = np.arange(0,40,10)
print(i)
j = np.tile(i,(4,3))
print(j)

k = np.array([[4,3,5],[1,2,1]])
print(k)
m = np.sort(k,axis=1)
#axis=1
print(m)
k.sort(axis=1)
print(k)
n = np.array([4,3,1,2])
l = np.argsort(n)
#argsort按照从小到大取index
print(l)
print(n[l])









