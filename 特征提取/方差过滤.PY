import pandas as pd
data = pd.read_excel(r"D:\python\datasets\基金公司基金资产净值.xlsx", sheet_name='Sheet2')
X = data.iloc[:,1:].dropna()
y = data.iloc[:,0]

from sklearn.feature_selection import VarianceThreshold
selector = VarianceThreshold() #实例化。不填参数默认方差为0
X_var0 = selector.fit_transform(X)
pd.DataFrame(X_var0).head()

import numpy as np
#np.median(X.var().values)

X_fscvar = VarianceThreshold(np.median(X.var().values)).fit_transform(X)

#若特征是伯努利随机变量，假设p=0.8,即二分类特征中某种分类占到80pct以上的时候删除特征
X_bvar = VarianceThreshold(.8*(1-.8)).fit_transform(X)
#print(X_bvar.shape)

from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.model_selection import cross_val_score
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

#假设我需要300个特征
X_fschi = SelectKBest(chi2,k=50).fit_transform(X_fscvar,y)
print(X_fschi.shape)

cross_val_score(RFC(n_estimators=10, random_state=10),X_fschi,y, cv=5).mean()

#如何设定超参数k
import matplotlib.pyplot as plt
score = []
for i in range(390,200,-10):
    X_fschi = SelectKBest(chi2,k=i).fit_transform(X_fscvar,y)
    once = cross_val_score(RFC(n_estimators=10, random_state=0),X_fschi,y,cv=5).mean()
    score.append(once)
plt.plot(range(350,200,-10),score)
plt.show()
