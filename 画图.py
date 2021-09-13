# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 10:00:07 2020

@author: zhou jian
"""



import matplotlib用法.pyplot as plt
import numpy as np
import pandas as pd
x = np.linspace(0, 10, 1000)
plt.figure()
plt.subplot(2, 1, 1) 
dffff = plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
print (dffff)