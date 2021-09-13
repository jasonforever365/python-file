import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import numpy as np

iris = load_iris()
y = iris.target
x = iris.data
#print(x.shape)

import pandas as pd
pd.DataFrame(x)

#建模。调用PCA
pca = PCA(n_components=2) #实例化
x_dr = pca.fit_transform(x)
#print(x_dr.shape)

#可视化
#布尔矩阵来区分三种鸢尾花
x_dr[y == 0, 0]

plt.figure()
#plt.scatter(x_dr[y == 0, 0], x_dr[y == 0, 1], c='red', label = iris.target_names[0])
#plt.scatter(x_dr[y == 1, 0], x_dr[y == 1, 1], c='black', label = iris.target_names[1])
#plt.scatter(x_dr[y == 2, 0], x_dr[y == 2, 1], c='orange', label = iris.target_names[2])
colors = ['red','black','orange']
for i in [0,1,2]:
    plt.scatter(
        x_dr[y == i, 0],
        x_dr[y == i, 1],
        alpha=.7, #alpha是指的点的透明度
        c = colors[i],
        label= iris.target_names[i]
    )

plt.legend()
plt.title('PCA of IRIS Dataset')
plt.show()

#属性explained_variance, 查看降维后每个新特征向量上所带的信息量大小（可解释性方差的大小）
print(pca.explained_variance_)

#属性pca.explained_variance_ratio,查看降维后每个新特征向量所占原始数据总信息量的百分比
#又叫做可解释方差贡献率
print(pca.explained_variance_ratio_)
print(pca.explained_variance_ratio_.sum())

pca_line = PCA().fit(x)
plt.plot([1,2,3,4],np.cumsum(pca_line.explained_variance_ratio_))
plt.xticks([1,2,3,4])
plt.xlabel("number of components after dimension reduction")
plt.ylabel("cumulative explained variance")
plt.show()

