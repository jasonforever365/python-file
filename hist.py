# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 16:19:50 2021

@author: zhou jian
"""


import pandas as pd
import matplotlib用法.pyplot as plt
from numpy import arange

reviews = pd.read_excel(r'C:\Users\zhou jian\Desktop\python\market.xlsx')
cols = ['开盘价(元)','最高价(元)','最低价(元)','收盘价(元)','成交额(百万)','成交量(股)']
norm_reviews = reviews[cols]
#print(norm_reviews[:1])

opening_price = norm_reviews['开盘价(元)'].value_counts()
opening_price = opening_price.sort_index()
selling_price = norm_reviews['收盘价(元)'].value_counts()
selling_price = selling_price.sort_index()
print(opening_price)
print(selling_price)

fig, ax=plt.subplots()
ax.hist(norm_reviews['开盘价(元)'], bins=20, edgecolor='black')
plt.show()