# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:31:01 2021

@author: zhou jian
"""

import pandas as pd
import matplotlib用法.pyplot as plt
from numpy import arange
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
reviews = pd.read_excel(r'C:\Users\zhou jian\Desktop\python\market.xlsx')
cols = ['开盘价(元)','最高价(元)','最低价(元)','收盘价(元)','成交额(百万)','成交量(股)']
norm_reviews = reviews[cols]
#print(norm_reviews[:1])


num_cols = [r'开盘价(元)',r'最高价(元)',r'最低价(元)',r'收盘价(元)']
#print(reviews[num_cols].head(3))
bar_heights = norm_reviews.loc[0, num_cols].values
#print(bar_heights)
bar_positions = arange(4) + 0.75
#bar_position是指每一个柱状图离X轴0值有多远
#print(bar_positions)
stock_positions = range(1,5)
fig, ax = plt.subplots()
ax.bar(bar_positions, bar_heights, width = 0.5)
#0.5指的是柱状图中柱的宽度
ax.set_xticks(stock_positions)
ax.set_xticklabels(num_cols,rotation=45)

ax.set_xlabel('set_pricing')
ax.set_ylabel('price')
ax.set_title('stock price')
plt.show()

