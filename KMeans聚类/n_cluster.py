from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

#make_blobs：自己创建数据集
X, y = make_blobs(n_samples=500, n_features=2, centers=4, random_state=1)

#fig, ax1 = plt.subplots(1)
#subplots(1): 生成一个子图；1:1个子图
#fig:画布；对象:ax1
#ax1.scatter(X[:,0],X[:,1]
           # ,marker='O' #点的形状
           # ,s=8 #点的大小
          # )
#plt.show()

#如果我们想看见这个点分布，怎么办
#color = ["red","pink","orange","gray"]
#fig,ax1 = plt.subplots(1)

#for i in range(4):
    #ax1.scatter(X[y==i,0],X[y==i,1]
               # ,marker='o'
               # ,s=8
               # ,c=color[i])
#plt.show()

n_clusters = 3
cluster = KMeans(n_clusters=n_clusters, random_state=0).fit(X)

#重要属性Labels_,查看聚好的类别，每个样本所对应的类
y_pred = cluster.labels_
y_pred

#KMeans因为并不需要建立模型或者预测结果，因此我们只需要fit就能够得到聚类结果
#KMeans也有接口predit和fit_predict，表示学习数据x并对x的类进行预测
#但所得到的结果和我们不调用predict，直接fit之后调用属性Labels一模一样
pre = cluster.fit_predict(X)

cluster_smallsub = KMeans(n_clusters=n_clusters,random_state=0).fit(X[:200])
y_pred_ = cluster_smallsub.predict(X)
#print(y_pred == y_pred_)
#验证通过Kmeans模拟出来的质心(500条选200条)和原标签的质心是否相同

#重要属性cluster_centers,查看质心
centroid = cluster.cluster_centers_

#重要属性inertia_,查看总距离平方和
inertia = cluster.inertia_

color = ["red","pink","orange","gray"]
fig,ax1 = plt.subplots(1)

for i in range(n_clusters):
    ax1.scatter(X[y==i,0],X[y==i,1]
               ,marker='o'
               ,s=8
               ,c=color[i])
ax1.scatter(centroid[:,0], centroid[:,1]
            , marker='x'
            , s=30
            , c="black")
plt.show()

#如果n_cluster = 其他值呢

n_clusters =5
cluster_ = KMeans(n_clusters=n_clusters, random_state=0).fit(X)
inertia = cluster_.inertia_
print(inertia_)

n_clusters =500
cluster_ = KMeans(n_clusters=n_clusters, random_state=0).fit(X)
inertia = cluster_.inertia_
print(inertia_)
#此时inertia = 0


