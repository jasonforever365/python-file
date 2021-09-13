# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 22:55:19 2021

@author: zhou jian
"""


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

#1.数据加载
data = pd.read_csv(r'C:\Users\zhou jian\Desktop\python\新建文本文档.csv')
data.info()
print(data.head(3))
#2.数据清理（缺失数据）
#3.特征工程（样本的特征和目标值分开）
y = data['price'] #目标值（标准答案）
x = data.drop('price', axis=1) #特征值
#drop里axis=0代表行，axis=1代表列
#4.数据拆分成训练集和测试集
#x_train: 特征值的训练集 y_train: 目标值的训练集
#x_train: 测试集的特征值 y_test:测试集的目标值
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size =0.25, random_state=1)
print(x_test)
print(y_test)
#test_size默认值为0.25
#5.根据不同的需求选择合适的模型
lr = LinearRegression()
#6. 训练模型，模型的一个调优
lr.fit(x_train, y_train)
# y = w*x + b （通过x与y,获取w和b）
print(lr.coef_, lr.intercept_)
#训练完毕获取权重和偏置，然后采用测试集的数据获取预测值
y_predict = lr.predict(x_test)
#预测值与真实值之间的差就是模型的误差
absoulte = np.absolute(y_predict - y_test)
mae = np.sum(absoulte)/len(y_test)
print('绝对值平均误差为',mae)
mae = mean_absolute_error(y_test, y_predict)
print('绝对值平均误差为',mae)
#显示模型的正确率
print('模型的正确率', lr.score(x_test, y_test))
#7. 模型的保存与使用





