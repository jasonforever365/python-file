from sklearn.metrics import silhouette_score
from sklearn.metrics import silhouette_samples
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

#make_blobs：自己创建数据集
X, y = make_blobs(n_samples=500, n_features=2, centers=4, random_state=1)

n_clusters = 3
cluster = KMeans(n_clusters=n_clusters, random_state=0).fit(X)

#重要属性Labels_,查看聚好的类别，每个样本所对应的类
y_pred = cluster.labels_
y_pred


n_clusters =4
cluster_ = KMeans(n_clusters=n_clusters, random_state=0).fit(X)

print(silhouette_score(X,y_pred))
print(silhouette_score(X,cluster_.labels_))
#silhouette_score返回轮廓系数的均值
#比较cluster为3和4的轮廓系数的值，是否下降

print(silhouette_samples(X,y_pred))
print(silhouette_samples(X,cluster_.labels_))
#silhouette_score返回轮廓系数的所有数据

from time import time
#time():记录每一次time()这行命令运行时刻的时间戳
t0 = time()
silhouette_score(X,y_pred)
print(time()-t0)