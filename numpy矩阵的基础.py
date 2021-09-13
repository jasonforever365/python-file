# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:33:39 2021

@author: zhou jian
"""


import numpy as np

#world_alcohol = np.genfromtxt('C:/Users/zhou jian/Desktop/python/world_alcohol.txt',delimiter=',',dtype=str)
#print(type(world_alcohol))
#print(world_alcohol)
#print(help(np.genfromtxt))

vector1 = np.array([1,2,3,4])
#print(vector1.shape)
#.shape: 显示几维
matrix = np.array([[5,10,15],[20,25,30]])
#print(matrix.shape)
#print(matrix[1,1])
#numpy里面行和列都是从0开始的
#print(vector1[0:3])
#print(matrix[:,1])

#寻找是否有10的程序
vector2 = np.array([5,10,15,20]) 
equal_to_ten = (vector2 == 10)
#print(equal_to_ten)
#print(vector2[equal_to_ten])

#寻找第二列是否为25的行
matrix2 = np.array([
    [5,10,15],
    [20,25,30],
    [35,40,45]
    ])
second_column_25 = (matrix2[:,1]==25)
#print(second_column_25)
#print(matrix2[second_column_25, :])

#改变NUMPY值的类型
vector3 = np.array(['1','2','3'])
#print(vector3.dtype)
#(vector3)
vector3 = vector3.astype(float)
#print(vector3.dtype)
#print(vector3) 

#求极值
#print(vector2.min())

#求和
#print(matrix2.sum(axis=1))
#axis=1是按照行来求和
#print(matrix2.sum(axis=0))
#axis=0是按照列来求和



