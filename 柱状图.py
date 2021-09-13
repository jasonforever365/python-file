# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 14:04:36 2021

@author: zhou jian
"""


import pandas as pd
import matplotlib用法.pyplot as plt
from numpy import arange
reviews = pd.read_excel(r'C:\Users\zhou jian\Desktop\python\market.xlsx')
cols = ['开盘价(元)','最高价(元)','最低价(元)','收盘价(元)','成交额(百万)','成交量(股)']
norm_reviews = reviews[cols]
#print(norm_reviews[:1])


num_cols = ['开盘价(元)','最高价(元)','最低价(元)','收盘价(元)']
#print(reviews[num_cols].head(3))
bar_heights = norm_reviews.loc[0, num_cols].values
#print(bar_heights)
bar_positions = arange(4) + 0.75
#bar_position是指每一个柱状图离X轴0值有多远
#print(bar_positions)
fig, ax = plt.subplots()
ax.bar(bar_positions, bar_heights, width = 0.5)
#0.5指的是柱状图中柱的宽度
plt.show()
