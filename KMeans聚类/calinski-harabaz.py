from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.metrics import calinski_harabasz_score

#make_blobs：自己创建数据集
X, y = make_blobs(n_samples=500, n_features=2, centers=4, random_state=1)

n_clusters = 3
cluster = KMeans(n_clusters=n_clusters, random_state=0).fit(X)

#重要属性Labels_,查看聚好的类别，每个样本所对应的类
y_pred = cluster.labels_
y_pred

print(calinski_harabasz_score(X,y_pred))

from time import time
#time():记录每一次time()这行命令运行时刻的时间戳
t0 = time()
calinski_harabasz_score(X,y_pred)
print(time()-t0)