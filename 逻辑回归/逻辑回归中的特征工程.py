from sklearn.linear_model import LogisticRegression as LR
from sklearn.datasets import load_breast_cancer
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.feature_selection import SelectFromModel

data = load_breast_cancer()
LR_ = LR(solver="liblinear",C=0.8,random_state=420)
cross_val_score(LR_,data.data, data.target, cv=10).mean()
#X_embedded = SelectFromModel(LR_,threshold=float, norm_order=1).fit_transform(data.data, data.target)
#特征数量减少到个位数，但模型效果仍然维持

LR_.fit(data.data,data.target).coef_

fullx = []
fsx = []

#此时我们的判断指标，就不是L1范数，而是逻辑回归中的系数了
threshold = np.linspace(0, abs(LR_.fit(data.data, data.target).coef_).max(),20)
#LR_.fit(data.data,data.target).coef_取绝对值，再取到最大值

k=0
for i in threshold:
    X_embedded = SelectFromModel(LR_,threshold=i).fit_transform(data.data, data.target)
    fullx.append(cross_val_score(LR_,data.data, data.target,cv=5).mean())
    fsx.append(cross_val_score(LR_,X_embedded, data.target,cv=5).mean())
    print((threshold[k],X_embedded.shape[1]))
    k+=1

plt.figure(figsize=(20,5))
plt.plot(threshold,fullx,label='full')
plt.plot(threshold,fsx,label='feature selection')
plt.xticks(threshold)
plt.legend()
plt.show()

