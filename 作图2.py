# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 23:48:11 2021

@author: zhou jian
"""


import pandas as pd
import matplotlib用法.pyplot as plt

zhongzheng = pd.read_excel(r'C:\Users\zhou jian\Desktop\python\中证500.xlsx')
zhongzheng['date'] = pd.to_datetime(zhongzheng['date'])
zhongzheng['Month'] = zhongzheng['date'].dt.month

fig = plt.figure(figsize=(6,3))
plt.plot(zhongzheng[0:12]['Month'],zhongzheng[0:12]['close'], c='red')
plt.plot(zhongzheng[12:24]['Month'],zhongzheng[12:24]['close'], c='yellow')

plt.show()