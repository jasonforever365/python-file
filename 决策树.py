# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 06:57:47 2021

@author: zhou jian
"""


from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import pandas as pd
import graphviz

wine = load_wine()
#print(wine.feature_names)
#pd.concat([pd.DataFrame(wine.data),pd.DataFrame(wine.target)], axis=1)
Xtrain, Xtest, Ytrain, Ytest=train_test_split(wine.data, wine.target,test_size=0.3)
clf =tree.DecisionTreeClassifier(criterion='entropy')
#第一步：实例化
clf = clf.fit(Xtrain, Ytrain)
score = clf.score(Xtest, Ytest)

feature_name=['alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 'proline']
dot_data= tree.export_graphviz(clf
                               ,feature_names=feature_name
                               ,class_names=['gin','sherry','bellmund']
                               ,filled=True
                               ,rounded=True)
graph = graphviz.Source(dot_data)
graph
clf.feature_importances_
[*zip(feature_name,clf.feature_importances_)]

#控制随机性,用random_state去控制随机数种子
clf=tree.DecisionTreeClassifier(criterion='entropy', random_state=30)
clf=clf.fit(Xtrain,Ytrain)
score=clf.score(Xtest,Ytest)
score #这个时候score总是一样

#splitter用来控制随机性
clf=tree.DecisionTreeClassifier(criterion='entropy'
                                , random_state=30
                                ,splitter='random')
clf=clf.fit(Xtrain,Ytrain)
score=clf.score(Xtest,Ytest)
score #这个时候score总是一样






