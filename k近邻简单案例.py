# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 07:35:28 2021

@author: zhou jian
"""


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

#1.数据获取screen
data = pd.read_csv(r'C:\Users\zhou jian\Desktop\python\movie data.csv')
data.info()
#2. 数据清理：缺省值，异常值，重复项
y = data['type']
X = data.drop(['type','name'], axis =1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
print(X_test)
print(y_test)
#n_neighbors设置邻居的数量
knn = KNeighborsClassifier(n_neighbors=3, weights='distance')
knn.fit(X_train,y_train)
#预测测试集
y_predict = knn.predict(X_test)
print('预测结果为', y_predict)
print('预测命中率',knn.score(X_test,y_test))
