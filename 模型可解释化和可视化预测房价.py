# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 09:35:34 2021

@author: zhou jian
"""


from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import numpy as np
from sklearn.utils import Bunch
# 非csv
lb = load_boston()
#print(lb, type(lb))
X = lb['data']
#特征值
y = lb['target']
#目标值
print(X.shape, y.shape)
#拆分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
lr = LinearRegression()
#把训练集交给模型
#y = w1*x1 + w2*x2 + ... + w13*x13 + b
lr.fit(X_train, y_train)
#训练的过程就是查找权重和偏置的过程
print(lr.coef_, lr.intercept_)
#通过查找的权重+偏置来预测测试集的目标值
y_predict = lr.predict(X_test)
#绝对值的平均误差
mae = np.sum(np.absolute(y_predict - y_test))/len(y_test)
print('mac误差为',mae)
mae = mean_absolute_error(y_test, y_predict)
print('mae误差为', mae)
#把误差转换成正确率
print('训练集的正确率', lr.score(X_train, y_train),'测试集的正确率', lr.score(X_test, y_test))
print('-'*100)
print(lr.coef_)
#默认的排序结果是从小到大
print(np.argsort(lr.coef_))
feature_names = lb['feature_names']
#从小到大获取特征值
print(feature_names[np.argsort(lr.coef_)])
print(lb['DESCR'])
print('-'*100)
#通过可视化的方式显示某个特征与价格之间的关系
import matplotlib用法.pyplot as plt

X = X[y < 50.00]
y = y[y < 50.00]
#X[行，列] X[:, [2,3,4]]
plt.rcParams['font.sans-serif'] = ['SimHei']  #matplotlib不能直接识别中文，需加该语句

def drawScatter(x, y, xlabel):
    plt.scatter(x,y)
    plt.xlabel(xlabel)
    plt.ylabel('房价')
    plt.title(f'{xlabel}与房价的散点图')
    plt.grid()
    plt.show()

drawScatter(X[:,5], y, '房间数')
drawScatter(X[:,4], y, '环保指标')







