# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 20:29:05 2021

@author: zhou jian
"""


from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
wine = load_wine()
print(wine.data.shape)

#实例化
#训练集代入实例化模型去进行训练，使用的借口是fit
#使用其他接口将测试集导入我们训练好的模型，去获取我们希望获取的结果（score, y_test）
from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data, wine.target, 
                                                test_size = 0.3)
clf = DecisionTreeClassifier(random_state=0)
rfc = RandomForestClassifier(random_state=0)
clf=clf.fit(Xtrain, Ytrain)
rfc=rfc.fit(Xtrain, Ytrain)

score_c = clf.score(Xtest, Ytest)
score_r = rfc.score(Xtest, Ytest)

print("Single Tree:{}".format(score_c), "Random Forest:{}".format(score_r))

#交叉验证: cross_val_score
from sklearn.model_selection import cross_val_score
import matplotlib用法.pyplot as plt

rfc = RandomForestClassifier(n_estimators=25)
rfc_s = cross_val_score(rfc, wine.data,wine.target,cv=10)

clf = DecisionTreeClassifier()
clf_s = cross_val_score(clf,wine.data,wine.target,cv=10)

#plt.plot(range(1,11),rfc_s,label='RandomForest')
#plt.plot(range(1,11),clf_s,label='DecisionTree')
#plt.legend()
#plt.show()

rfc_l = []
clf_l = []

for i in range(10):
    rfc = RandomForestClassifier(n_estimators=25)
    rfc_s = cross_val_score(rfc,wine.data,wine.target,cv=10).mean()
    rfc_l.append(rfc_s)
    clf=DecisionTreeClassifier()
    clf_s=cross_val_score(clf, wine.data,wine.target,cv=10).mean()
    clf_l.append(clf_s)
    
#plt.plot(range(1,11),rfc_l,label='Random Forest')
#plt.plot(range(1,11),clf_l,label='Decision Tree') 
#plt.legend()
#plt.show()
   
    
#n_estimator的参数设置
superpa = []
for i in range(20):
    rfc = RandomForestClassifier(n_estimators=i+1, n_jobs=-1)    
    rfc_s = cross_val_score(rfc, wine.data, wine.target, cv=10).mean()
    superpa.append(rfc_s)
#print(max(superpa),superpa.index(max(superpa))+1)
#打印出列表中最大值以及其index的位置（需要+1）
#plt.figure(figsize=[20,5])
#plt.plot(range(1,21),superpa)
#plt.show()

#装袋法
import numpy as np
from scipy.special import comb

np.array([comb(25,i)*(0.2**i)*((1-0.2)**(25-i)) for i in range(13,26)]).sum()
rfc = RandomForestClassifier(n_estimators=25,random_state=2)
rfc = rfc.fit(Xtrain, Ytrain)    
#随机森林的重要属性之一：estimators_, 查看森林中树的状况
print(rfc.estimators_)
rfc.estimators_[0].random_state
for i in range(len(rfc.estimators_)):
    print(rfc.estimators_[i].random_state)
    
