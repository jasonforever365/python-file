# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 19:51:41 2021

@author: zhou jian
"""


import pandas as pd
from pandas import Series

HS300_stock = pd.read_excel(r'C:/Users/zhou jian/Desktop/datasets/market.xlsx')
open_price = HS300_stock['开盘价(元)']
#print(type(open_price))
#print(open_price[0:5])

series_open_price = open_price.values
print(type(series_open_price))
closing_price = HS300_stock['收盘价(元)']
series_closing_price = closing_price.values
series_table = Series(series_closing_price, index=series_open_price)
series_table[['1272.65','1272.65']]