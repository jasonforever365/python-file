from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = load_breast_cancer()

#rfc=RandomForestClassifier(n_estimators=100,random_state=90) #实例化
#score_pre = cross_val_score(rfc,data,data.target, cv=10).mean()

#选择学习曲线的方法：能看见趋势，看n_estimators在什么取值下变得平稳，即观察n_estimators的变化如何引起模型的整体准确率的变化
#一般设为200,而不是50,但运算量大，耗时间长

#scorel = []
#for i in range(0, 50, 10):
    #rfc = RandomForestClassifier(n_estimators=i+1,
                                # n_jobs=-1,
                                 #random_state=90)
    #score = cross_val_score(rfc, data.data, data.target, cv=10).mean()
    #scorel.append(score)

#打印scorel列表的最大值，和该对象（最大值）在list里的索引
#print(max(scorel),(scorel.index(max(scorel))*10)+1)

#plt.figure(figsize=[20,5])
#plt.plot(range(1,51,10),scorel)
#plt.show()

#list.index[object]
#返回这个object在列表List的索引
#40-41左右达到峰值

#scorel = []
#for i in range(35, 45):
    #rfc = RandomForestClassifier(n_estimators=i+1,
                                 #n_jobs=-1,
                                 #random_state=90)
    #score = cross_val_score(rfc, data.data, data.target, cv=10).mean()
    #scorel.append(score)

#打印scorel列表的最大值，和该对象（最大值）在list里的索引
#print(max(scorel),([*range(35,45)][scorel.index(max(scorel))])

#plt.figure(figsize=[20,5])
#plt.plot(range(35,45),scorel)
#plt.show()

#调整max_depth
#param_grid = {'max_depth': np.arange(1,20,1)}

#一般根据数据的大小进行试探，乳腺癌数据很小，那么可以采用1-10,或1-20这样的数据进行试探
#但对于像digit recognition那样的大型数据来说，应尝试30-50层深度
#应画出学习曲线，来观察深度对模型的影响

#rfc = RandomForestClassifier(n_estimators=39,
                             #random_state=90)

#GS = GridSearchCV(rfc,param_grid,cv=10)
#GS.fit(data.data, data.target)

#print(GS.best_params_)
#print(GS.best_score_)

#调整min_samples_leaf
param_grid = {'min_samples_leaf': np.arange(1,1+10,1)}

#一般根据数据的大小进行试探，乳腺癌数据很小，那么可以采用1-10,或1-20这样的数据进行试探
#但对于像digit recognition那样的大型数据来说，应尝试30-50层深度
#应画出学习曲线，来观察深度对模型的影响

rfc = RandomForestClassifier(n_estimators=39,
                             random_state=90)

GS = GridSearchCV(rfc,param_grid,cv=10)
GS.fit(data.data, data.target)

print(GS.best_params_)
print(GS.best_score_)

#其他参数按照相同的代码进行调参，比价GS.best_score_
#总结：先调整n_estimators, 然后是max_depth，来判断模型位于复杂度-泛化误差图像的哪一边，从而选择我们应该调整的参数的方向