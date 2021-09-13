# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 23:02:41 2021

@author: zhou jian
"""


import pandas as pd
import matplotlib用法.pyplot as plt

zhongzheng = pd.read_excel(r'C:\Users\zhou jian\Desktop\python\中证500.xlsx')
zhongzheng['date'] = pd.to_datetime(zhongzheng['date'])
print(zhongzheng.head(12))

first_twelve = zhongzheng[0:12]
plt.plot(first_twelve['date'], first_twelve['close'])
plt.xticks(rotation=45)
#X轴的标斜着写，rotation=45表示旋转45度
plt.xlabel('date')
plt.ylabel('close price')
plt.title('every day closing price')
plt.show()