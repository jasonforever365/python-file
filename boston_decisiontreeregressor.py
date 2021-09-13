# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 21:01:41 2021

@author: zhou jian
"""

from sklearn.datasets import load_boston
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor

boston = load_boston()
#实例化
regressor = DecisionTreeRegressor(random_state=0) 
cross_val_score(regressor, boston.data, boston.target, cv=10,
                #scoring="neg_mean_squared_error"
                )
#cross_val_score：交叉验证