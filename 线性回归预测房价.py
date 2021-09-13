# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 14:45:37 2021

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






