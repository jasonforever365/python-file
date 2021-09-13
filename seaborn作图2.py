# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 08:46:40 2021

@author: zhou jian
"""


import numpy as np
import matplotlib用法.pyplot as plt
import seaborn as sns
from scipy import stats, integrate
import pandas as pd

#x =np.random.normal(size=100)
#sns.distplot(x, kde=False)
#sns.distplot(x, bins=10, kde=False) #bins:设置矩形图数量

#x =np.random.gamma(6, size=200)
#sns.distplot(x, kde=False, fit=stats.gamma) #fit:控制拟合的参数分布图形

#mean, cov=[0,1],[(1, .5),(.5,1)]
#data =np.random.multivariate_normal(mean, cov, 200)
#df =pd.DataFrame(data, columns=['x','y'])
#sns.jointplot(x='x', y='y',data=df)

mean, cov=[0,1],[(1, .5),(.5,1)]
x, y =np.random.multivariate_normal(mean, cov, 1000).T
with sns.axes_style('white'):
    sns.jointplot(x=x, y=y, kind='hex', color='k')