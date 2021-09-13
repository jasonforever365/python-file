# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:29:43 2021

@author: zhou jian
"""


import numpy as np
import pandas as pd
import matplotlib用法 as mpl
import matplotlib用法.pyplot as plt
import seaborn as sns

sns.set(color_codes=True)
np.random.seed(sum(map(ord, 'regression')))

tips=sns.load_dataset('tips')
#tips.head()

#regplot和lmplot()都可以绘制回归关系
#sns.regplot(x='total_bill', y ='tip', data=tips)
#sns.lmplot(x='total_bill', y ='tip', data=tips)
sns.regplot(x='size', y ='tip', data=tips, x_jitter=0.05)
#x_jitter: 表示沿轴随机分布，相对避免重叠
