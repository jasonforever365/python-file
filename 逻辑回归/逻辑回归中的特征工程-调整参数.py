from sklearn.linear_model import LogisticRegression as LR
from sklearn.datasets import load_breast_cancer
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.feature_selection import SelectFromModel

data = load_breast_cancer()

fullx = []
fsx = []

C = np.arange(0.01,10.01,0.5)

for i in C:
    LR_ = LR(solver="liblinear", C=i, random_state=420)
    fullx.append(cross_val_score(LR_,data.data, data.target,cv=10).mean())
    X_embedded = SelectFromModel(LR_, norm_order=1).fit_transform(data.data, data.target)
    fsx.append(cross_val_score(LR_,X_embedded, data.target,cv=10).mean())
    print(max(fsx),C[fsx.index(max(fsx))])
    #打印出fsx中最大值和最大值在列表的索引

plt.figure(figsize=(20,5))
plt.plot(C,fullx,label='full')
plt.plot(C,fsx,label='feature selection')
plt.xticks(C)
plt.legend()
plt.show()

#测试的结果在7.01效果最好，那么进一步取值

fullx = []
fsx = []

C = np.arange(6.05,7.05,0.005)

for i in C:
    LR_ = LR(solver="liblinear", C=i, random_state=420)
    fullx.append(cross_val_score(LR_,data.data, data.target,cv=10).mean())
    X_embedded = SelectFromModel(LR_, norm_order=1).fit_transform(data.data, data.target)
    fsx.append(cross_val_score(LR_,X_embedded, data.target,cv=10).mean())
    print(max(fsx),C[fsx.index(max(fsx))])
    #打印出fsx中最大值和最大值在列表的索引

plt.figure(figsize=(20,5))
plt.plot(C,fullx,label='full')
plt.plot(C,fsx,label='feature selection')
plt.xticks(C)
plt.legend()
plt.show()