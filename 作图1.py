# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 23:38:45 2021

@author: zhou jian
"""


import matplotlib用法.pyplot as plt
import numpy as np
fig = plt.figure(figsize=(3,3))
#figsize: 长和宽
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(np.random.randint(1,5,5),np.arange(5))
ax2.plot(np.arange(10)*3, np.arange(10))
plt.show()