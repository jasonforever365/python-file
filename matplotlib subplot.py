# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 23:16:41 2021

@author: zhou jian
"""


import matplotlib用法.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(4,3,1)
ax2 = fig.add_subplot(4,3,2)
ax3 = fig.add_subplot(4,3,11)
#创建了一个x*y的矩阵，图的具体位置在z处
#subplot(x,y,z)
plt.show()