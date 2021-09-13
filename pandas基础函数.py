# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 20:12:19 2021

@author: zhou jian
"""


import pandas as pd
import numpy as np


HS300_stock = pd.read_excel(r'C:/Users/zhou jian/Desktop/datasets/market.xlsx')
HS300_stock_index = HS300_stock.set_index('日期',drop=False)
#print(HS300_stock_index.index)
HS300_stock_calculate = HS300_stock[['开盘价(元)','收盘价(元)']]
modify_HS_HS300_stock_calculate = HS300_stock_calculate.apply(lambda x: np.std(x), axis=1)
print(modify_HS_HS300_stock_calculate)
