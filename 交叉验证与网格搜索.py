# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 07:38:43 2021

@author: zhou jian
"""

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_digits
import pandas as pd
import matplotlib用法.pyplot as plt
from sklearn.model_selection import GridSearchCV


#1. 数据获取scrapy
digits = load_digits()
#print(digits, type(digits))
#print(digits['DESCR'])
X = digits['data']
y = digits['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
#超参数：机器模型在训练之前必须指定的参数,可采用网格搜索来找出最优的超参数
knn = KNeighborsClassifier()
#cv=2 则是两则交叉验证
gc = GridSearchCV(estimator=knn,param_grid={'n_neighbors':[5,7,10],'weights':['uniform','distance']},cv=2)
#模型训练
gc.fit(X_train, y_train)
y_predict = gc.predict(X_test)
#交叉验证与网络搜索相关结果如下：
print('交叉验证与网格搜索最优的模型',gc.best_score_)
print('交叉验证打印结果',gc.cv_results_)
