# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 23:45:03 2021

@author: zhou jian
"""


import matplotlib用法.pyplot as plt
import numpy as np
#在指定范围内，随机生成size个随机数(代表特征值)
x = np.random.uniform(-3, 3, size=100)
print(x,x.shape)
#模拟目标值（x）与y并不是简单的线性关系
y = 0.5*x**2 + x +2 +np.random.normal(0,1,size=100)
#plt.scatter(x,y)
#plt.show()
#采用线性回归的方程来预测
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
#训练模型（为了方便没有拆封训练集和测试集）
X = x.reshape(-1, 1)
print(X.shape)
#一维矩阵转化为二维矩阵
lr.fit(X,y)
#训练过程就是寻找最佳权重和偏置的过程
print('权重',lr.coef_,'偏置',lr.intercept_)
y_predict = lr.predict(X)
plt.scatter(x, y)
#生成了线形图，观察预测值与真实值的误差
plt.plot(x,y_predict, color='r')
plt.show()


#y = w*x + b ===> y= w1*x**2 + w2*x + b
print((x**2).shape)
#hstack在水平方向追加，vstack在垂直方向叠加
X2 = np.hstack([X**2,X])
print(X2.shape)
#线性回归的模型进行训练
lr = LinearRegression()
lr.fit(X2, y)
#训练过程就是寻找最佳权重和偏置的过程
print('权重', lr.coef_, '偏置', lr.intercept_)
y_predict = lr.predict(X2)
#真实的数据集采用散点图显示
plt.scatter(x,y)
#预测数据集，采用线型图显示,必须按照x轴从小到大进行绘制
plt.plot(np.sort(x),y_predict[np.argsort(x)],color='r')
plt.show()











