# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 08:15:56 2021

@author: zhou jian
"""


import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib用法.pyplot as plt

#创造一条含有噪声的正弦曲线
rng =np.random.RandomState(1)
X = np.sort(5*rng.rand(80,1),axis=0)
#rng.rand():生产一个80行一列的随机数（必须是二维数组，不能是一维数组），随机数在（0,1）之间
y = np.sin(X).ravel()
#ravel():降维
y[::5] += 3*(0.5 - rng.rand(16))
#这一步是正弦曲线加上噪声
#y[::5]: y数组里每5个数加一个噪音
plt.figure()
plt.scatter(X,y,s=20,edgecolors='black', c='darkorange', label='data')

#导入训练集
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_1.fit(X,y)
regr_2.fit(X,y)

#导入测试集
X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
#[:, np.newaxis]:升维
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)

#绘制图像
plt.figure()
plt.scatter(X, y, s=20, edgecolors='black',c = 'darkorange', label='data')
plt.plot(X_test, y_1, color='blue', label='max_depth=2',linewidth=2)
plt.plot(X_test, y_2, color='yellowgreen', label='max_depth=5',linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title('Decision Tree Regression')
plt.legend()
plt.show()

