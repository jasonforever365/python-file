# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:39:11 2021

@author: zhou jian
"""


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_digits
import pandas as pd
import matplotlib用法.pyplot as plt


#1. 数据获取scrapy
digits = load_digits()
#print(digits, type(digits))
#print(digits['DESCR'])
X = digits['data']
y = digits['target']
#print(X, X.shape)
#rint(y, y.shape)
#显示第九章图的特征值和目标值
#digit = X[9]
#digit_image = digit.reshape(8,8)
#plt.imshow(digit_image)
#plt.show()
#print(y[9])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
#超参数：机器模型在训练之前必须指定的参数 n_neighbors
#模型参数：算法训练的过程中学习的参数，KNN没有模型参数，只有超参数
#y =w*x + b ===> w,b就是模型参数
knn = KNeighborsClassifier(n_neighbors=3, weights='distance')
#模型训练
knn.fit(X_train, y_train)
y_predict = knn.predict(X_test)
print('命中率', knn.score(X_train, y_train))