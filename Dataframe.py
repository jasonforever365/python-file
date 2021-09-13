# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 15:34:59 2021

@author: zhou jian
"""


import pandas as pd

df = pd.DataFrame({'id':[1,2,3], 'Name':['Tim', 'Victor', 'Engie']})
df = df.set_index('id')
df.to_excel(r'C:\Users\zhou jian\Desktop\python\output.xlsx')
print('Done!')

