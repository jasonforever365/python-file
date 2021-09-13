# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:09:41 2021

@author: zhou jian
"""


import numpy as np
#[2, 4] dot [4,1] ===> [2,1]
t1 = np.arange(8).reshape(2,4)
print(t1)
#w权重的矩阵
t2 = np.arange(4).reshape(4,1)
print(t2)
t3 = t1.dot(t2)
print(t3)
#t3就是线性预测值
