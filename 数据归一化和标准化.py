# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 09:30:45 2021

@author: zhou jian
"""


from sklearn.preprocessing import MinMaxScaler, StandardScaler

mn = MinMaxScaler()
#归一化
data = mn.fit_transform([[90,2,10,40], [60,4,15,45],[75,3,13,46]])
print('归一化之后的数据\n', data)
data = mn.inverse_transform(data)
print('原始数据\n', data)
print('-'*10)

std = StandardScaler()
#标准化
data = std.fit_transform([[90,2,10,40], [60,4,15,45],[75,3,13,46]])
print('每列特征的平均值', std.mean_)
print('标准化之后的数据\n', data)
data = mn.inverse_transform(data)
print('原始数据\n', data)