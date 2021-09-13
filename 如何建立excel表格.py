# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 20:26:11 2021

@author: zhou jian
"""


import pandas as pd

s1 = pd.Series([1,2,3],index=[1,2,3],name='A')
s2 = pd.Series([10,20,30],index=[1,2,3],name='B')
s3 = pd.Series([100,200,300],index=[1,2,3],name='C')

df = pd.DataFrame({s1.name:s1, s2.name:s2, s3.name:s3})
#df = pd.DataFrame([s1, s2, s3]) #这种情况下s1,s2,s3变成行
print(df)
