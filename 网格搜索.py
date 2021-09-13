# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 15:24:20 2021

@author: zhou jian
"""

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib用法.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score

data = pd.read_csv(r'C:\Users\zhou jian\Desktop\datasets\Titanic.csv')
#data.info()
data.drop(["Cabin",'Name','Ticket'],inplace=True,axis=1)

#处理缺失值
data['Age'] = data['Age'].fillna(data['Age'].mean())
data = data.dropna()
#data.info()
labels = data['Embarked'].unique().tolist()
data['Embarked'] = data['Embarked'].apply(lambda x: labels.index(x))
#unique删掉重复值
#x是指的data['Embarked']里的每一行数据
data['Sex'] = (data['Sex'] == 'male').astype('int')

X = data.iloc[:, data.columns !='Survived']
y = data.iloc[:, data.columns =='Survived']
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.3)

#训练之后的index是无序的，这一步是调整序号，使其有序
for i in [Xtrain, Xtest, ytrain, ytest]:
    i.index=range(i.shape[0])

clf = DecisionTreeClassifier(random_state=25)
clf = clf.fit(Xtrain, ytrain)
score = clf.score(Xtest, ytest)    
print(score)

clf = DecisionTreeClassifier(random_state=25)
score = cross_val_score(clf, X, y, cv=10).mean()
print(score)

#由于显示的交叉验证的得分较低，需要调整参数
tr = [] #训练集的结果
te = [] #测试集的结果
for i in range(10):
    clf = DecisionTreeClassifier(random_state=25
                                 ,max_depth=i+1
                                 ,criterion='entropy'
                                 )
    clf = clf.fit(Xtrain, ytrain)
    score_tr  = clf.score(Xtrain, ytrain)
    score_te = cross_val_score(clf, X, y, cv=10).mean()
    tr.append(score_tr)
    te.append(score_te)
print(max(te))

plt.plot(range(1,11), tr, color='red',label='train')
plt.plot(range(1,11), te, color='blue',label='test')
plt.xticks(range(1,11))
plt.legend()
plt.show()

#网格搜素：枚举技术，同时调整多个参数的技术
#一串参数和参数对应的，我们希望网格搜索来搜索的参数的取值范围

parameters = {"criterion":('gini', 'entropy')
              ,'splitter':('best','random')
              ,'max_depth':[*range(1,10)]
              ,'min_samples_leaf':[*range(1,50,5)]
              ,'min_impurity_decrease':[*np.linspace(0,0.5,50)]}
clf = DecisionTreeClassifier(random_state=25)
GS =GridSearchCV(clf, parameters, cv=10)
GS = GS.fit(Xtrain, ytrain)

GS.best_params_ #从我们输入的参数和参数取值的列表中，返回最佳组合
GS.best_score_ #网格搜索后的模型的评判标准



   
    
    
    
    
    
    

