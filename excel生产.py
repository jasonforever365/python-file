# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 16:30:38 2021

@author: zhou jian
"""


import pandas as pd
people = pd.read_excel(r'C:\Users\zhou jian\Desktop\python\SCF liandong 2018 till 20200915.xlsx', index_col='业务品种')
#print(people.shape)
#people.column = ['业务品种','业务编号'] 设置column的reference
#print(people.columns)
#print(people.head(3))
#print(people.tail(3))
people.to_excel(r'C:\Users\zhou jian\Desktop\python\SCF liandong 2018 till 2021017.xlsx')